import base64
import io
import json5    
import os
import shutil
import threading
import time
import zipfile






from network_manager import NetworkManager
class Client:
    def __init__(self, steamworks, password, host='127.0.0.1', tcp_port=65432, udp_port=65433, keep_alive_interval=5):
        self.steamworks = steamworks
        
        self.network = NetworkManager(host, tcp_port, udp_port)
        self.keep_alive_interval = keep_alive_interval
        self.running = True
        self.last_frame = 0

        # Connection process
        self.network.connect_tcp()
        self.network.bind_udp()

        auth_message = {"username": self.steamworks.Users.GetSteamID(), "password": password, "udp_port": self.network.udp_port}
        self.network.send_tcp(auth_message)
        response = self.network.receive_tcp()
        server_info = json5.loads(response)

        server_id = server_info.get("server_id")
        self.ensure_save_folder_from_server_id(server_id)

        self.keep_alive_thread = threading.Thread(target=self.send_keep_alive, daemon=True)
        self.udp_thread = threading.Thread(target=self.listen_for_udp_updates, daemon=True)
        self.tcp_thread = threading.Thread(target=self.listen_for_tcp_messages, daemon=True)

        self.keep_alive_thread.start()
        self.udp_thread.start()
        self.tcp_thread.start()
        
    

            


    def ensure_save_folder_from_server_id(self, server_id: str, template_path: str = "base_lua") -> str:
        """
        Ensures a save folder exists using the server-provided ID.
        Populates it with template files if it's a new folder.
        """
        save_path = os.path.join("saves", server_id)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            if os.path.exists(template_path):
                for item in os.listdir(template_path):
                    src = os.path.join(template_path, item)
                    dst = os.path.join(save_path, item)
                    if os.path.isfile(src):
                        shutil.copy2(src, dst)
        self.server_id = server_id
        return save_path


    def send_keep_alive(self):
        """Send keep-alive messages periodically."""
        while self.running:
            try:
                time.sleep(self.keep_alive_interval)
                self.network.send_tcp({"type": "keep_alive"})
            except Exception as e:
                print(f"Keep-alive error: {e}")
                self.running = False

    def listen_for_udp_updates(self):
        """Listen for UDP updates from the server."""
        try:
            while self.running:
                state, server_address = self.network.receive_udp()
                if state["frame"] > self.last_frame:
                    self.last_frame = state["frame"]
                    print(f"Received frame {state['frame']}: {state}")
                else:
                    print(f"Ignored outdated frame {state['frame']}")
        except Exception as e:
            print(f"UDP listener error: {e}")
            self.running = False

    def listen_for_tcp_messages(self):
        """Listen for TCP messages from the server."""
        buffer = ""
        while self.running:
            try:
                data = self.network.receive_tcp()
                buffer += data
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    print(f"message {message}")
                    print(f"Received: {json5.loads(message)}")
            except Exception as e:
                print(f"TCP listener error: {e}")
                
                self.running = False

    def shutdown(self):
        print("in shutdown")
        """Shut down the client."""
        self.running = False
        self.network.close()
        
        if self.keep_alive_thread is not None:
            self.keep_alive_thread.join(timeout=2)
        if self.udp_thread is not None:
            self.udp_thread.join(timeout=2)
        if self.tcp_thread is not None:
            self.tcp_thread.join(timeout=2)
        
        print("Client has stopped.")


    def upload_save_folder(self):
        save_folder = os.path.join("saves", self.server_id)
        
        # Create a zip in memory
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(save_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, save_folder)
                    zipf.write(full_path, rel_path)
    
        buffer.seek(0)
        zipped_data = buffer.read()
        
        chunk_size = 1024
        total_chunks = (len(zipped_data) + chunk_size - 1) // chunk_size
    
        for i in range(total_chunks):
            chunk = zipped_data[i * chunk_size : (i + 1) * chunk_size]
            chunk_b64 = base64.b64encode(chunk).decode("utf-8")
    
            message = {
                "type": "file_upload",
                "chunk_index": i,
                "total_chunks": total_chunks,
                "payload_type": "zip_chunk",
                "payload": chunk_b64
            }
            self.network.send_tcp(message)