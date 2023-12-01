import unittest
from entities.entry import Entry
from repositories.reference_repository import ReferenceRepository
from entities.book import Book
from entities.manual import Manual
from services.db_connection import get_database_connection
from initialize_database import create_tables, drop_tables

import os


class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"

class TestBook(unittest.TestCase):
    def setUp(self):

        testconnection = get_database_connection(testing=True)
        self.repo = ReferenceRepository(testconnection)
        drop_tables(testconnection)
        create_tables(testconnection)

        book_data = {"author": "a",
                     "title": "b",
                     "publisher": "c",
                     "year": 2014,
                     "volume": 1,
                     "series": "d",
                     "address": "e",
                     "edition": 2,
                     "month": 3,
                     "note": "f"
                     }

        manual_data = {"title": "a",
                       "author": "c",
                       "year": 2000,
                       "month": "g",
                       "address": "e",
                       "note": "h",
                       "organization": "d",
                       "edition": "f"

                       }

        self.book = Entry(book_data, Book(), MockKeygen())
        self.manual = Entry(manual_data, Manual(), MockKeygen())

        self.repo.save_entry(self.book)
        self.repo.save_entry(self.manual)

    def test_fetch(self):
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
}\n@manual{a999,
  title = "a",
  year = 2000,
  month = "g",
  address = "e",
  note = "h",
  organization = "d",
  edition = "f",
  author = "c"
}\n"""
        f = self.repo.fetch()
        self.assertEqual(f, correct_answer)

    def tearDown(self):
        drop_tables(self.testconnection)
