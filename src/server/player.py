class Player:
    def __init__(self, username, is_human=True):
        self.username = username
        self.is_human = is_human
        self.client = None  # To track the connected client socket