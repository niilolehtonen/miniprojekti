from random import randrange

class KeyGenerator:

    def generate_key(self, title:str):
        return f"{title.split(' ')[0]}{randrange(999999999)}"
    