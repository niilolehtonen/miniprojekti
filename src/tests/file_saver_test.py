import os
import unittest

from entities.book import Book
from entities.entry import Entry
from repositories.reference_repository import ReferenceRepository
from services.db_connection import get_database_connection
from initialize_database import create_tables, drop_tables

class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"


class TestBook(unittest.TestCase):
    def setUp(self):

        self.testconnection = get_database_connection(testing=True)
        self.repo = ReferenceRepository(self.testconnection)
        drop_tables(self.testconnection)
        create_tables(self.testconnection)

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

    def test_save(self):

        correct_answer = [
            'book entry: ',
            'author: a',
            'title: b',
            'publisher: c',
            'year: 2014',
            'volume: 1',
            'series: d',
            'address: e',
            'edition: 2',
            'month: 3',
            'note: f',
            '',
            '',
            '',
        ]

        self.repo.save_entry(self.book)
        f = self.repo.as_human_readable()
        f = f.split("\n")
        self.assertEqual(f, correct_answer)


    def tearDown(self):
        drop_tables(self.testconnection)
