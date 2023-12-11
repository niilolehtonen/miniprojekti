class Manual:

    def get_required_fields(self):
        return [("title", str)]

    def get_optional_fields(self):
        return [("year", int), ("month", int), ("address", str), ("month", int), ("note", str), ("organization", str),
                ("edition", str), ("author", str)]

    def get_type(self):
        return "manual"
