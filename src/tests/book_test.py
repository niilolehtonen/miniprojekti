import unittest
from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c","d",2014,"e")

    def test_format(self):
        correct_answer = """@book{e,
  author    = "a",
  title     = "b",
  publisher = "c",
  address   = "d",
  year      = 2014
}"""
        self.assertEqual(correct_answer,self.book.format())