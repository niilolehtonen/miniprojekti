from entities.book import Book
from entities.entry import Entry
from entities.key_generator import KeyGenerator
from repositories.reference_repository import ReferenceRepository
from services.db_connection import get_database_connection

books = [
    {
        "author": "Wake, Alan",
        "title": "Alex Casey",
        "publisher": "Lake publishing",
        "year": "2010"
    }, {
        "author": "Wake, Alan",
        "title": "What I Can't Forget",
        "publisher": "Lake publishing",
        "year": "2010"
    }, {
        "author": "Wake, Alan",
        "title": "Return to Sender",
        "publisher": "Lake publishing",
        "year": "2010"
    }, {
        "author": "Wake, Alan",
        "title": "The Things That I Want",
        "publisher": "Lake publishing",
        "year": "2010"
    }, {
        "author": "Wake, Alan",
        "title": "The Fall of Casey",
        "publisher": "Lake publishing",
        "year": "2010"
    }, {
        "author": "Wake, Alan",
        "title": "The Sudden Stop",
        "publisher": "Lake publishing",
        "year": "2010"
    },
]


def main():
    connection = get_database_connection()
    reference_repository = ReferenceRepository(connection, KeyGenerator())

    for book_data in books:
        reference_repository.save_entry(Entry(book_data, Book(), KeyGenerator))


if __name__ == "__main__":
    main()
