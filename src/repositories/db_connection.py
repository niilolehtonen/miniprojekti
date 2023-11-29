import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()

entry_list = [address,annote,author,booktitle,chapter,crossref,doi,edition,editor,email,howpublished,institution,journal,month,note,number,organisation,pages,publisher,school,series,title,Type,volume,year]



cursor.execute("CREATE TABLE IF NOT EXISTS entries(
                id INTEGER PRIMARY KEY UNIQUE,
                ref_type TEXT
                " )