from singleton import Singleton


class Log(Singleton):
    def __init__(self, max_size=None):
        if max_size:
            self.max_size = max_size
        self.records = []

    def record(self, record):
        self.records.append(record)

    def get(self, last_lines=5):
        last_lines = min(last_lines, len(self.records))
        return "\n".join(self.records[(len(self.records) - last_lines):])