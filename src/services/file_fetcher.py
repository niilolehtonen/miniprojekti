class FileFetcher:
    def __init__ (self):
        pass

    def fetch (self):
        with open("data.bib", "r") as file:
            f = file.read()
        return f