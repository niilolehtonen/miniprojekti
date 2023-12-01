from entities.entry import Entry
from entities.key_generator import KeyGenerator


class Book:

    def get_required_fields(self):
        return [("author", str), ("title", str), ("publisher", str), ("year", int)]

    def get_optional_fields(self):
        return [("volume", int), ("series", str), ("address", str), ("edition", int), ("month", int), ("note", str)]

    def get_type(self):
        return "book"
