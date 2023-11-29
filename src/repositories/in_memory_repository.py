class InMemoryRepository:
    def __init__(self):
        self.entries = []

    def save_entry(self, entry):
        self.entries.append(entry)

    def fetch(self):
        ret = ""
        for entry in self.entries:
            ret += entry.format() + "\n\n"
        return ret

    def as_human_readable(self):
        ret = ""
        for entry in self.entries:
            ret += entry.as_human_readable() + "\n\n"
        return ret