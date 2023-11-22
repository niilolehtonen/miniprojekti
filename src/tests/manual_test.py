import unittest
from entities.manual import Manual

class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"

class TestEntry(unittest.TestCase):
    def setUp(self):
        self.manual = Manual("a",2000,"c","d","e","f","g","h", MockKeygen())

    def test_manual_creation(self):
        test_string = """@manual{a999,
  title        = "a",
  author       = "c",
  year         = 2000,
  month        = "g",
  address      = "e",
  note         = "h",
  organization = "d",
  edition      = "f"
}"""
        self.assertEqual(self.manual.format(), test_string)
        
