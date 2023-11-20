import unittest
from entities.book import Entry

class TestEntry(unittest.TestCase):
    def setUp(self):
        self.entry = Entry()

    def test_Key_generator(self):
        self.assertEqual(self.entry.generate_key("Jenson B. A., Sheldon M.", 2014), "Jenson2014")