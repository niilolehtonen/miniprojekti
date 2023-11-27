class UserInputError(Exception):
    pass

class Validator:

    def __init__(self):
        pass

    def validate_book(self,info):
        if info["author"] == None:
            raise UserInputError("Author field is empty")
        if info["title"] == None:
            raise UserInputError("Title field is empty")
        if info["publisher"] == None:
            raise UserInputError("Publisher field is empty")
        if info["year"] == None:
            raise UserInputError("Year field is empty")

    def validate_manual(self,info):
        if info["title"] == None:
            raise UserInputError("Title field is empty")
