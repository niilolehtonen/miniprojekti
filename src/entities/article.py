class Article:

    def get_required_fields(self):
        return [("author", str), ("title", str), ("journal", str), ("year", int)]
    
    def get_optional_fields(self):
        return [("volume", int), ("number", int), ("pages", str), ("month", int), ("note", str)]
    
    def get_type(self):
        return "article"