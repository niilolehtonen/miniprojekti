import re

class UserInputError(Exception):
    pass

class Validator:
    def __init__(self):
        pass

    def validate_book(self, info):
        errors = []
        if info["author"] is None:
            raise UserInputError("Author field is empty")
        if info["title"] is None:
            raise UserInputError("Title field is empty")
        if info["publisher"] is None:
            raise UserInputError("Publisher field is empty")
        if info["year"] is None:
            raise UserInputError("Year field is empty")

        if re.match(r"[a-zA-Z]+$", info["author"]) is None:
            errors.append("Author should contain only letters")

        if re.match(r"^\d+$", info["year"]) is None:
            errors.append("Year should contain only numbers")

        if "volume" in info and info["volume"] != "" and re.match(r"^\d+$", info["volume"]) is None:
            errors.append("Volume should contain only numbers")

        if "month" in info and info["month"] != "" and re.match(r"^(0?[1-9]|1[0-2])$", info["month"]) is None:
            errors.append("Month should contain only numbers 1 to 12")

        return errors

    def validate_manual(self, info):
        errors = []
        if info["title"] is None:
            raise UserInputError("Title field is empty")

        if "author" in info and info["author"] != "" and re.match(r"[a-zA-Z]+$", info["author"]) is None:
            errors.append("Author should contain only letters")

        if "year" in info and info["year"] != "" and re.match(r"^\d+$", info["year"]) is None:
            errors.append("Year should contain only numbers")

        if "month" in info and info["month"] != "" and re.match(r"^(0?[1-9]|1[0-2])$", info["month"]) is None:
            errors.append("Month should contain only numbers 1 to 12")

        return errors

    def validate_article(self, info)
        errors = []

        if info["author"] is None:
            raise UserInputError("Author field is empty")
        if info["title"] is None:
            raise UserInputError("Title field is empty")
        if info["journal"] is None:
            raise UserInputError("Journal field is empty")
        if info["year"] is None:
            raise UserInputError("Year field is empty")

        if re.match(r"[a-zA-Z]+$", info["author"]) is None:
            errors.append("Author should contain only letters")

        if re.match(r"^\d+$", info["year"]) is None:
            errors.append("Year should contain only numbers")

        if "volume" in info and info["volume"] != "" and re.match(r"^\d+$", info["volume"]) is None:
            errors.append("Volume should contain only numbers")

        if "number" in info and info["number"] != "" and re.match(r"^\d+$", info["volume"]) is None:
            errors.append("Number should contain only numbers")

        if "month" in info and info["month"] != "" and re.match(r"^(0?[1-9]|1[0-2])$", info["month"]) is None:
            errors.append("Month should contain only numbers 1 to 12")

        return errors
