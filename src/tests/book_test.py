import unittest
from entities.book import Book
from entities.entry import Entry


class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"


class TestBook(unittest.TestCase):
    def setUp(self):
        # self.book = Book("a","b","c",2014, 1, "d", "e", 2, 3, "f", MockKeygen())
        data = {"author": "a", "title": "b", "publisher": "c", "year": 2014, "volume": 1, "series": "d", "address": "e",
                "edition": 2, "month": 3, "note": "f"}
        self.book = Entry(data, Book(), MockKeygen())

    def test_format(self):
            correct_answer = """@book{b999,
  author    = "a",
  title     = "b",
  publisher = "c",
  year      = 2014,
  volume    = 1,
  series    = "d",
  address   = "e",
  edition   = 2,
  month     = 3,
  note      = "f"
}"""
            self.assertEqual(correct_answer, self.book.format())
