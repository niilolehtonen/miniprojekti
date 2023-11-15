class Book:
    def __init__ (self, input_author, input_title, input_publisher, input_address, input_year, input_key):
        self.input_author = input_author
        self.input_title = input_title
        self.input_publisher = input_publisher
        self.input_address = input_address
        self.input_year = input_year
        self.input_key = input_key

    def format_input(self):
        formated = "@book{" + self.input_key
        formated += ",\n  author    = \"" + self.input_author
        formated += "\",\n  title     = \"" + self.input_title
        formated += "\",\n  publisher = \"" + self.input_publisher
        formated += "\",\n  address   = \"" + self.input_address
        formated += "\",\n  year      = " + self.input_year
        formated += "\n}"

        return formated