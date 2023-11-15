class FileSaver:
    def __init__(self, filename):
        self.filename = filename

    def save(self, book):
        with open(self.filename, "a") as file:
            file.write(book.format_input() + "\n")
            