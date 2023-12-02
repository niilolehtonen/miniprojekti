import sqlite3

connection = sqlite3.connect("database.db", check_same_thread=False)
connection.row_factory = sqlite3.Row

def get_database_connection(testing=False):
    if testing:
        testconnection = sqlite3.connect("testdatabase.db", check_same_thread=False)
        testconnection.row_factory = sqlite3.Row
        return testconnection
    return connection
