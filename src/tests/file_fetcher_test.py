import unittest
from entities.book import Book
from services.file_saver import FileSaver
from services.file_fetcher import FileFetcher
import os

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","a","a","a",2000,"a")
        self.book2 = Book("b","b","b","b",2000,"b")
        self.saver = FileSaver("testdata.bib")

        self.book.format()
        self.book2.format()
        self.saver.save(self.book)
        self.saver.save(self.book2)

        self.fetcher = FileFetcher("testdata.bib")

    def test_fetch(self):
        correct_answer = """@book{a,
  author    = "a",
  title     = "a",
  publisher = "a",
  address   = "a",
  year      = 2000
}\n@book{b,
  author    = "b",
  title     = "b",
  publisher = "b",
  address   = "b",
  year      = 2000
}\n"""
        f = self.fetcher.fetch()
        self.assertEqual(f,correct_answer)

    def tearDown(self):    
        os.remove("testdata.bib")