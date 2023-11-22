from entities.entry import Entry

class Manual(Entry):
    def __init__ (self, input_title:str, 
                  input_year:int, 
                  input_author:str, 
                  input_organization:str, 
                  input_address:str, 
                  input_edition:str,
                  input_month:str,
                  input_note:str
                  ):
        self.title = input_title
        self.year = input_year
        self.author = input_author
        self.organization = input_organization
        self.address = input_address
        self.edition = input_edition
        self.month = input_month
        self.note = input_note

    def format(self):
        formated = "@manual{" + super().generate_key(self.author,self.year) + ","
        formated += "\n  title        = \"" + self.title + "\","
        formated += "\n  author       = \"" + self.author + "\","
        formated += "\n  year         = " + str(self.year) + ","
        formated += "\n  month        = \"" + str(self.month) + "\","
        formated += "\n  address      = \"" + self.address + "\","
        formated += "\n  note         = \"" + self.note + "\","
        formated += "\n  organization = \"" + self.organization + "\","
        formated += "\n  edition      = \"" + str(self.edition) + "\""
        formated += "\n}"

        return formated