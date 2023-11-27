import os
import unittest

from entities.book import Book
from entities.entry import Entry
from repositories.reference_repository import ReferenceRepository


class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"


class TestBook(unittest.TestCase):
    def setUp(self):
        data = {"author": "a",
                "title": "b",
                "publisher": "c",
                "year": 2014,
                "volume": 1,
                "series": "d",
                "address": "e",
                "edition": 2,
                "month": 3,
                "note": "f"}

        self.book = Entry(data, Book(), MockKeygen())
        self.saver = ReferenceRepository("testdata.bib")

    def test_save(self):
        correct_answer = """@book{b999,
  author = "a",
  title = "b",
  publisher = "c",
  year = 2014,
  volume = 1,
  series = "d",
  address = "e",
  edition = 2,
  month = 3,
  note = "f"
}\n"""
        self.book.format()
        self.saver.save_entry(self.book)
        with open("testdata.bib") as file:
            f = file.read()
        self.assertEqual(f, correct_answer)

    def tearDown(self):
        os.remove("testdata.bib")
