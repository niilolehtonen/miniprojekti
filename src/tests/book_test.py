import unittest
from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c",2014, 1, "d", "e", 2, 3, "f")

    def test_format(self):
        correct_answer = """@book{a2014,
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
        self.assertEqual(correct_answer,self.book.format())