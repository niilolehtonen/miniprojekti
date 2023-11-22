import unittest

from repositories.reference_repository import ReferenceRepository
from entities.book import Book

import os


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","a","a",2000, 1, "a", "a", 2, 3, "a")
        self.book2 = Book("b","b","b",2000, 4, "b", "b", 5, 6, "b")
        self.repo = ReferenceRepository("testdata.bib")

        self.book.format()
        self.book2.format()
        self.repo.save_book(self.book)
        self.repo.save_book(self.book2)

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
}\n@book{b2000,
  author    = "b",
  title     = "b",
  publisher = "b",
  year      = 2000,
  volume    = 4,
  series    = "b",
  address   = "b",
  edition   = 5,
  month     = 6,
  note      = "b"
}\n"""
        f = self.repo.fetch()
        self.assertEqual(f, correct_answer)

    def tearDown(self):
        os.remove("testdata.bib")
