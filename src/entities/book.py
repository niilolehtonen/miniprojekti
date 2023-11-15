class Book:
    def __init__ (self, input_author:str, input_title:str, input_publisher:str, input_address:str, input_year:int, input_key:str):
        self.input_author = input_author
        self.input_title = input_title
        self.input_publisher = input_publisher
        self.input_address = input_address
        self.input_year = input_year
        self.input_key = input_key

    def format(self):
        formated = "@book{" + self.input_key
        formated += ",\n  author    = \"" + self.input_author
        formated += "\",\n  title     = \"" + self.input_title
        formated += "\",\n  publisher = \"" + self.input_publisher
        formated += "\",\n  address   = \"" + self.input_address
        formated += "\",\n  year      = " + str(self.input_year)
        formated += "\n}"

        return formated