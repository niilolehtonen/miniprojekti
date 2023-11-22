import unittest
from entities.book import Book
from services.file_saver import FileSaver
import os

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c",2014, 1, "d", "e", 2, 3, "f")
        self.saver = FileSaver("testdata.bib")

    def test_save(self):
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
}\n"""
        self.book.format()
        self.saver.save(self.book)
        with open("testdata.bib") as file:
            f = file.read()
        self.assertEqual(f,correct_answer)

    def tearDown(self):    
        os.remove("testdata.bib")