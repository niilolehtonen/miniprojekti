from entities.book import Book

class UserInputError(Exception):
    pass

class Validator:

    def __init__(self):
        pass

    def validate_book(author,title,publisher,year,volume,series,address,edition,month,note):
        if author != str or author == "":
            raise UserInputError("Input not accepted on field 'Author'")
        if title != str or title == "":
            raise UserInputError("Input not accepted on field 'Title'")
        if publisher != str or publisher == "":
            raise UserInputError("Input not accepted on field 'Publisher'")
        if year != int or year == "":
            raise UserInputError("Input not accepted on field 'Year'")
        if volume != int:
            raise UserInputError("Input not accepted on field 'Volume'")
        if series != str:
            raise UserInputError("Input not accepted on field 'Series'")
        if address != str:
            raise UserInputError("Input not accepted on field 'Address'")
        if edition != int:
            raise UserInputError("Input not accepted on field 'Edition'")
        if month != int:
            raise UserInputError("Input not accepted on field 'Month'")
        if note != str:
            raise UserInputError("Input not accepted on field 'Note'")
        
        return None
    
    def validate_manual(author,title,year,organization,address,edition,month,note):
        if author != str or author == "":
            raise UserInputError("Input not accepted on field 'Author'")
        if title != str:
            raise UserInputError("Input not accepted on field 'Title'")
        if  organization != str:
            raise UserInputError("Input not accepted on field 'Organization'")
        if year != int:
            raise UserInputError("Input not accepted on field 'Year'")
        if address != str:
            raise UserInputError("Input not accepted on field 'Address'")
        if edition != int:
            raise UserInputError("Input not accepted on field 'Edition'")
        if month != int:
            raise UserInputError("Input not accepted on field 'Month'")
        if note != str:
            raise UserInputError("Input not accepted on field 'Note'")
        
        return None