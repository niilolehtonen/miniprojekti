from entities.entry import Entry

class Book(Entry):
    def __init__ (self, input_author:str, 
                  input_title:str, 
                  input_publisher:str, 
                  input_address:str, 
                  input_year:int):
        self.author = input_author
        self.title = input_title
        self.publisher = input_publisher
        self.address = input_address
        self.year = input_year

    def format(self):
        formated = "@book{" + super().generate_key(self.author, str(self.year))
        formated +=   ",\n  author    = \"" + self.author
        formated += "\",\n  title     = \"" + self.title
        formated += "\",\n  publisher = \"" + self.publisher
        formated += "\",\n  address   = \"" + self.address
        formated += "\",\n  year      = " + str(self.year)
        formated += "\n}"

        return formated