from entities.entry import Entry

class Book(Entry):
    def __init__ (self, input_author:str, 
                  input_title:str, 
                  input_publisher:str, 
                  input_year:int,
                  input_volume:int,
                  input_series:str,
                  input_address:str,
                  input_edition:int,
                  input_month:int,
                  input_note:str,):
        self.author = input_author
        self.title = input_title
        self.publisher = input_publisher
        self.year = input_year
        self.volume = input_volume
        self.series = input_series
        self.address = input_address
        self.edition = input_edition
        self.month = input_month
        self.note = input_note

    def format(self):
        formated = "@book{" + super().generate_key(self.title)
        formated +=   ",\n  author    = \"" + self.author
        formated += "\",\n  title     = \"" + self.title
        formated += "\",\n  publisher = \"" + self.publisher
        formated += "\",\n  year      = " + str(self.year)
        formated += ",\n  volume    = " + str(self.volume)
        formated += ",\n  series    = \"" + self.series
        formated += "\",\n  address   = \"" + self.address
        formated += "\",\n  edition   = " + str(self.edition)
        formated += ",\n  month     = " + str(self.month)
        formated += ",\n  note      = \"" + self.note
        formated += "\"\n}"

        return formated