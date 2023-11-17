class FileFetcher:
    def __init__ (self, filename):
        self.filename = filename

    def fetch (self):
        with open(self.filename, "r") as file:
            f = file.read()
        return f