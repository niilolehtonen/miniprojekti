import unittest

from repositories.reference_repository import ReferenceRepository
from entities.book import Book
from entities.manual import Manual

import os


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","a","a",2000, 1, "a", "a", 2, 3, "a")
        self.manual = Manual("b", 2000, "b", "b", "b", 4, 5, "b")
        self.repo = ReferenceRepository("testdata.bib")

        self.book.format()
        self.manual.format()
        self.repo.save_book(self.book)
        self.repo.save_manual(self.manual)

    def test_fetch(self):
        correct_answer = """@book{a2000,
  author    = "a",
  title     = "a",
  publisher = "a",
  year      = 2000,
  volume    = 1,
  series    = "a",
  address   = "a",
  edition   = 2,
  month     = 3,
  note      = "a"
}\n@manual{b2000,
  title         = "b",
  author        = "b",
  year          = 2000,
  month         = 4,
  address       = "b",
  note          = "b",
  organization  = "b",
  edition       = 5,
}\n"""
        f = self.repo.fetch()
        self.assertEqual(f, correct_answer)

    def tearDown(self):
        os.remove("testdata.bib")
