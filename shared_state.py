import threading

class SharedState:
    def __init__(self):
        self.state = False
        self.lock = threading.Lock()

    def set(self, value):
        with self.lock:
            self.state = value

    def get(self):
        with self.lock:
            return self.state
