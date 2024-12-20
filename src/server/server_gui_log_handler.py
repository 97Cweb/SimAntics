import logging

class ServerGUILogHandler(logging.Handler):
    def __init__(self, gui):
        super().__init__()
        self.gui = gui
        # Set the formatter to include only the timestamp and message
        self.setFormatter(logging.Formatter('%(asctime)s', datefmt='%Y-%m-%d %H:%M:%S'))

    def emit(self, record):
        if self.gui is None:
            return  # Exit early if gui reference is None
        timestamp = self.format(record)  # Get only the timestamp
        color_map = {
            "DEBUG": "gray",
            "INFO": "black",
            "WARNING": "orange",
            "ERROR": "red",
        }
        color = color_map.get(record.levelname, "black")
        # Format the log message with timestamp, color-coded log level, and message
        formatted_message = f"{timestamp} <font color='{color}'>[{record.levelname.capitalize()}]</font> {record.msg}"
        self.gui.update_logs(formatted_message)
        
    def close(self):
        """Release any resources held by this handler."""
        if hasattr(self, "gui"):
            self.gui = None  # Clear reference to avoid cyclic dependencies
        super().close()