import socket
import json5

class NetworkManager:
    def __init__(self, host, tcp_port, udp_port):
        self.host = host
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.tcp_client = None
        self.udp_socket = None

    def connect_tcp(self):
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.connect((self.host, self.tcp_port))
        print("Connected to TCP server.")

    def bind_udp(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.host, self.udp_port))
        print("UDP socket bound.")

    def send_tcp(self, message):
        self.tcp_client.sendall(json5.dumps(message).encode('utf-8'))

    def receive_tcp(self):
        return self.tcp_client.recv(4096).decode('utf-8')

    def send_udp(self, message, server_address):
        self.udp_socket.sendto(json5.dumps(message).encode('utf-8'), server_address)

    def receive_udp(self):
        data, server_address = self.udp_socket.recvfrom(4096)
        return json5.loads(data.decode('utf-8')), server_address

    def close(self):
        if self.tcp_client:
            self.tcp_client.close()
        if self.udp_socket:
            self.udp_socket.close()
        print("Network connections closed.")