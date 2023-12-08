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


    def test_nonempty_optional_fields_are_being_added_to_entry_data(self):
        test_data = {"author": "A", "title": "B", "publisher": "C", "year": 2000, "series": "D"}
        entry = Entry(test_data, Book(), MockKeygen())

        self.assertIn("series", entry.data.keys())


    def test_empty_optional_fields_are_not_added_to_entry_data(self):
        test_data = {"author": "A", "title": "B", "publisher": "C", "year": 2000, "series": ""}
        entry = Entry(test_data, Book(), MockKeygen())

        self.assertNotIn("series", entry.data.keys())


    def test_field_formating_adds_quotation_marks_to_a_string(self):
        test_data = {"author": "A", "title": "B", "publisher": "C", "year": 2000, "series": ""}
        entry = Entry(test_data, Book(), MockKeygen())

        self.assertEqual(entry._Entry__format_field("address", "northpole"), '"northpole"')


    def test_field_formating_return_empty_if_key_not_found(self):
        test_data = {"author": "A", "title": "B", "publisher": "C", "year": 2000}
        entry = Entry(test_data, Book(), MockKeygen())

        self.assertEqual(entry._Entry__format_field("dog's name", "fluffy"), "")