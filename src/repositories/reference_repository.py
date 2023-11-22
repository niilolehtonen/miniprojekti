class ReferenceRepository:
    def __init__(self, filename=None):
        self.filename = filename

    def save_book(self, book):
        with open(self.filename, "a") as file:
            file.write(book.format() + "\n")

    def save_manual(self, manual):
        with open(self.filename, "a") as file:
            file.write(manual.format() + "\n")

    def fetch(self):
        with open(self.filename, "r") as file:
            f = file.read()
        return f
