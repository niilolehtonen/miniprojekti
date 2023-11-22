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

        self.assertEqual(self.validator.validate_book(self.info), None)
    
    def test_validate_book_author_not_given(self):
        self.info["author"] = None
        self.info["title"] = "Algorimit"
        self.info["publisher"] = "MIT"
        self.info["year"] = "2018"

        with self.assertRaises(UserInputError):
            self.validator.validate_book(self.info)

    def test_validate_manual_correct(self):
        self.info["title"] = "Ohjeet"

        self.assertEqual(self.validator.validate_manual(self.info), None)

    def test_validate_manual_title_not_given(self):
        self.info["title"] = None

        with self.assertRaises(UserInputError):
            self.validator.validate_manual(self.info)
