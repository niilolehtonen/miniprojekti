import unittest
from entities.article import Article
from entities.entry import Entry


class MockKeygen:
    def generate_key(self, title):
        return f"{title.split(' ')[0]}{999}"


class TestBook(unittest.TestCase):
    def setUp(self):
        # self.book = Book("a","b","c",2014, 1, "d", "e", 2, 3, "f", MockKeygen())
        data = {"author": "a", "title": "b", "journal": "c", "year": 2014, "volume": "1", "number": "2",
                "pages": "20-25", "month": 3, "note": "f"}
        self.article = Entry(data, Article(), MockKeygen())

    def test_format(self):
            correct_answer = """@article{b999,
  author = "a",
  title = "b",
  journal = "c",
  year = 2014,
  volume = "1",
  number = "2",
  pages = "20-25",
  month = 3,
  note = "f"
}"""
            self.assertEqual(correct_answer, self.article.format())