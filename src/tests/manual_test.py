import unittest

from entities.entry import Entry
from entities.manual import Manual


class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"


class TestEntry(unittest.TestCase):
    def setUp(self):
        data = {"title": "a",
                "author": "c",
                "year": 2000,
                "month": "g",
                "address": "e",
                "note": "h",
                "organization": "d",
                "edition": "f"}

        self.manual = Entry(data, Manual(), MockKeygen())

    def test_manual_creation(self):
        test_string = """@manual{a999,
  title = "a",
  year = 2000,
  month = "g",
  address = "e",
  note = "h",
  organization = "d",
  edition = "f",
  author = "c"
}"""

        self.assertEqual(self.manual.format(), test_string)
