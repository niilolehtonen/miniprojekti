class Entry:

    def __init__(self):
        pass

    def generate_key(self, author:str, year:int):
        return f"{author.split(' ')[0]}{str(year)}"