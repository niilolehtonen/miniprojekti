import unittest
from entities.manual import Manual

class TestEntry(unittest.TestCase):
    def setUp(self):
        self.manual = Manual("a",2000,"c","d","e","f","g","h")

    def test_manual_creation(self):
        test_string = "@manual{c2000,\n"+"  title        = \"a\",\n"+"  author       = \"c\",\n"+"  year         = \"2000\",\n"+"  month        = \"g\",\n"+"  address      = \"e\",\n"+"  note         = \"h\",\n"+"  organization = \"d\",\n"+"  edition      = \"f\",\n"+"}"
        self.assertEqual(self.manual.format(), test_string)
        
