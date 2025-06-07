import threading
import time
from collections import defaultdict

class MessageThrottler:
    """
    A helper to collect and throttle repetitive messages per user.
    Sends batched messages at regular intervals.
    """
    def __init__(self, send_callback, interval=1.0):
        """
        Args:
            send_callback (function): Function to send batched messages.
                                      It must take (username, message) as arguments.
            interval (float): Time interval (in seconds) to batch messages.
        """
        self.send_callback = send_callback  # Function to send messages
        self.interval = interval            # Time interval for batching
        self.user_message_counts = defaultdict(lambda: defaultdict(int))
        self.lock = threading.Lock()
        self.running = True

        # Start the message processing thread
        self.thread = threading.Thread(target=self._process_messages, daemon=True)
        self.thread.start()

    def add_message(self, username, message):
        """
        Add a message to be throttled for a specific user.

        Args:
            username (str): The recipient's username.
            message (str): The message content to throttle.
        """
        with self.lock:
            self.user_message_counts[username][message] += 1

    def _process_messages(self):
        """
        Internal thread function to process batched messages at intervals.
        """
        while self.running:
            time.sleep(self.interval)
            with self.lock:
                for username, messages in self.user_message_counts.items():
                    for message, count in messages.items():
                        if count == 1:
                            self.send_callback(username, message)
                        else:
                            self.send_callback(username, f"{message} (x{count})")
                self.user_message_counts.clear()

    def stop(self):
        """Stop the message throttler."""
        self.running = False
        self.thread.join()
