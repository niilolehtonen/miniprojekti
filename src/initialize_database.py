from services.db_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists entries;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            ref_type TEXT,
            address TEXT,
            annote TEXT,
            author TEXT,
            booktitle TEXT,
            chapter TEXT,
            crossref TEXT,
            doi TEXT,
            edition TEXT,
            editor TEXT,
            email TEXT,
            howpublished TEXT,
            institution TEXT,
            journal TEXT,
            month TEXT,
            note TEXT,
            number TEXT,
            organization TEXT,
            pages TEXT,
            publisher TEXT,
            school TEXT,
            series TEXT,
            title TEXT,
            Type TEXT,
            volume TEXT,
            year TEXT
            )
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()