from entities.entry import Entry


class Manual:
    #    def __init__(self, input_title: str,
    #                 input_year: int,
    #                 input_author: str,
    #                 input_organization: str,
    #                 input_address: str,
    #                 input_edition: str,
    #                 input_month: str,
    #                 input_note: str,
    #                 keygen
    #                 ):
    #        self.keygen = keygen
    #
    #        self.title = input_title
    #        self.year = input_year
    #        self.author = input_author
    #        self.organization = input_organization
    #        self.address = input_address
    #        self.edition = input_edition
    #        self.month = input_month
    #        self.note = input_note
    #
    #    def format(self):
    #        formated = "@manual{" + self.keygen.generate_key(self.title) + ","
    #        formated += "\n  title        = \"" + self.title + "\","
    #        formated += "\n  author       = \"" + self.author + "\","
    #        formated += "\n  year         = " + str(self.year) + ","
    #        formated += "\n  month        = \"" + str(self.month) + "\","
    #        formated += "\n  address      = \"" + self.address + "\","
    #        formated += "\n  note         = \"" + self.note + "\","
    #        formated += "\n  organization = \"" + self.organization + "\","
    #        formated += "\n  edition      = \"" + str(self.edition) + "\""
    #        formated += "\n}"
    #
    #        return formated

    def get_required_fields(self):
        return [("title", str)]

    def get_optional_fields(self):
        return [("year", int), ("month", str), ("address", str), ("month", int), ("note", str), ("organization", str),
                ("edition", str), ("author", str)]

    def get_type(self):
        return "manual"
