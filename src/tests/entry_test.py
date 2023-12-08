import unittest
from entities.entry import Entry
from entities.book import Book

class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"

class TestEntry(unittest.TestCase):
    def setUp(self):
        pass

    def test_execption_raises_when_required_field_is_none(self):
        test_data = {"author": "A", "title": "B", "publisher": None, "year": 2000}
        
        with self.assertRaises(Exception) as context:
            entry = Entry(test_data, Book(), MockKeygen())

        self.assertEqual(str(context.exception), "publisher not found")