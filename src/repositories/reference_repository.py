from entities.entry import Entry
from entities.key_generator import KeyGenerator
from entities.book import Book
from entities.manual import Manual

class ReferenceRepository:
    def __init__(self, connection):
        self._connection = connection
        self._keygen = KeyGenerator()

    def save_entry(self, entry):
        cursor = self._connection.cursor()

        fields = "ref_type,"
        values = f'"{entry.get_type()}",'

        for i in entry.data.keys():
            fields += f"{i},"
            values += f'"{entry.data[i]}",'

        fields = fields[:-1]
        values = values[:-1]

        cursor.execute(f"INSERT INTO ENTRIES ({fields}) VALUES ({values})")
        self._connection.commit()

    def fetch(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM ENTRIES")
        rows = cursor.fetchall()
        entries = (Entry(row, self.type_checker(row["ref_type"]), self._keygen) for row in rows)
        formatted = ""
        for entry in entries:
            formatted += entry.format()
        return formatted

    def type_checker(self, ref_type):
        types = {"book": Book(), "manual": Manual()}
        return types[ref_type]

    def as_human_readable(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM ENTRIES")
        rows = cursor.fetchall()
        entries = (Entry(row, self.type_checker(row["ref_type"]), self._keygen) for row in rows)
        ret = ""
        for entry in entries:
            ret += entry.as_human_readable() + "\n\n"
        return ret
