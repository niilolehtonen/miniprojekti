import unittest
from services.validator import Validator, UserInputError


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()
        self.info = {}

    def test_validate_book_correct(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"

        self.assertEqual(self.validator.validate_book(self.info), [])

    def test_validate_book_author_not_given(self):
        self.info["author"] = None
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"

        with self.assertRaises(UserInputError):
            self.validator.validate_book(self.info)

    def test_validate_book_title_not_given(self):
        self.info["author"] = "Timo"
        self.info["title"] = None
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"

        with self.assertRaises(UserInputError):
            self.validator.validate_book(self.info)    

    def test_validate_book_publisher_not_given(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = None
        self.info["year"] = "2018"

        with self.assertRaises(UserInputError):
            self.validator.validate_book(self.info)

    def test_validate_book_year_not_given(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = None

        with self.assertRaises(UserInputError):
            self.validator.validate_book(self.info)

    def test_validate_book_invalid_author(self):
        self.info["author"] = "34"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"

        errors = self.validator.validate_book(self.info)
        self.assertIn("Author should contain only letters", errors)

    def test_validate_book_invalid_year(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "year"

        errors = self.validator.validate_book(self.info)
        self.assertIn("Year should contain only numbers", errors)

    def test_validate_book_invalid_year(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"
        self.info["volume"] = "first"

        errors = self.validator.validate_book(self.info)
        self.assertIn("Volume should contain only numbers", errors)

    def test_validate_book_invalid_month(self):
        self.info["author"] = "Timo"
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "year"
        self.info["month"] = "20"

        errors = self.validator.validate_book(self.info)
        self.assertIn("Month should contain only numbers 1 to 12", errors)

    def test_validate_manual_correct(self):
        self.info["title"] = "Ohjeet"

        self.assertEqual(self.validator.validate_manual(self.info), [])

    def test_validate_manual_title_not_given(self):
        self.info["title"] = None

        with self.assertRaises(UserInputError):
            self.validator.validate_manual(self.info)

    def test_validate_manual_invalid_author(self):
        self.info["title"] = "Ohjeet"
        self.info["author"] = "23"

        errors = self.validator.validate_manual(self.info)
        self.assertIn("Author should contain only letters", errors)

    def test_validate_manual_invalid_year(self):
        self.info["title"] = "Ohjeet"
        self.info["year"] = "vuosi"

        errors = self.validator.validate_manual(self.info)
        self.assertIn("Year should contain only numbers", errors)

    def test_validate_manual_invalid_month(self):
        self.info["title"] = "Ohjeet"
        self.info["month"] = "23"

        errors = self.validator.validate_manual(self.info)
        self.assertIn("Month should contain only numbers 1 to 12", errors)

    def test_validate_article_correct(self):
        self.info["author"] = "Author"
        self.info["title"] = "Title"
        self.info["journal"] = "Journal"
        self.info["year"] = "2023"
        self.assertEqual(self.validator.validate_article(self.info),[])
    
    def test_validate_article_missing_required_info(self):
        self.info = {"author": "A", "title": "B", "journal": "C", "year" : "2023"}
        for field in self.info:
            req = self.info.copy()
            req[field] = None
            with self.assertRaises(UserInputError):
                self.validator.validate_article(req)

    def test_validate_article_author_contains_illegal_cahracters(self):
        self.info = {"author": "B12", "title": "B", "journal": "C", "year" : "2023"}
        errors = self.validator.validate_article(self.info)
        self.assertIn("Author should contain only letters", errors)

    def test_validate_article_illegal_characters(self):
        self.info = {"author": "A", "title": "B", "journal": "C", "year" : "2023",
                    "year": "2023A", "volume": "**S*", "number": "24ji", "month": "13"}
        errors = self.validator.validate_article(self.info)
        self.assertIn("Year should contain only numbers", errors)
        self.assertIn("Volume should contain only numbers", errors)
        self.assertIn("Number should contain only numbers", errors)
        self.assertIn("Month should contain only numbers 1 to 12", errors)
