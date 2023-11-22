import unittest

from repositories.reference_repository import ReferenceRepository
from entities.book import Book
from entities.manual import Manual

import os


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c",2014, 1, "d", "e", 2, 3, "f")
        self.manual = Manual("a",2000,"c","d","e","f","g","h")
        self.repo = ReferenceRepository("testdata.bib")

        self.book.format()
        self.manual.format()
        self.repo.save_book(self.book)
        self.repo.save_manual(self.manual)

    def test_fetch(self):
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
}\n@manual{c2000,
  title        = "a",
  author       = "c",
  year         = 2000,
  month        = "g",
  address      = "e",
  note         = "h",
  organization = "d",
  edition      = "f"
}\n"""
        f = self.repo.fetch()
        self.assertEqual(f, correct_answer)

    def tearDown(self):
        os.remove("testdata.bib")
