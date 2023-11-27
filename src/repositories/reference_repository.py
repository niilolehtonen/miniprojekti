class ReferenceRepository:
    def __init__(self, filename=None):
        self.filename = filename

    def save_entry(self, entry):
        with open(self.filename, "a") as file:
            file.write(entry.format() + "\n")

    def fetch(self):
        with open(self.filename, "r") as file:
            f = file.read()
        return f
