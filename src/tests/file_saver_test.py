import unittest
from entities.book import Book
from services.file_saver import FileSaver
import os

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c","d",2014,"e")
        self.saver = FileSaver("testdata.bib")

    def test_save(self):
        correct_answer = """@book{e,
  author    = "a",
  title     = "b",
  publisher = "c",
  address   = "d",
  year      = 2014
}\n"""
        self.book.format()
        self.saver.save(self.book)
        with open("testdata.bib") as file:
            f = file.read()
        self.assertEqual(f,correct_answer)

    def tearDown(self):    
        os.remove("testdata.bib")