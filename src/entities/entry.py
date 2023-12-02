class Entry:
    def __init__(self, input_data: dict, entry_type, keygen):
        self.entry_type = entry_type
        self.data = {}
        self.keygen = keygen
        for required_field in entry_type.get_required_fields():
            if required_field[0] not in input_data.keys() or input_data[required_field[0]] is None:
                raise required_field[0] + "not found"
            self.data[required_field[0]] = input_data[required_field[0]]

        for optional_field in entry_type.get_optional_fields():
            if optional_field[0] in input_data.keys() and input_data[optional_field[0]] is not None and input_data[optional_field[0]] != "":
                self.data[optional_field[0]] = input_data[optional_field[0]]

    def get_type(self):
        return self.entry_type.get_type()

    def format(self):
        formatted = "@" + self.get_type() + "{" + self.keygen.generate_key(self.data["title"]) + ",\n"
        items = list(self.data.items())
        for i in range(len(items) - 1):
            item = items[i]
            formatted += "  " + item[0] + " = " + self.__format_field(item[0], item[1]) + ",\n"
        formatted += "  " + items[-1][0] + " = " + self.__format_field(items[-1][0], items[-1][1]) + "\n"
        formatted += "}"
        return formatted

    def __format_field(self, key, value):
        fields = []
        fields.extend(self.entry_type.get_required_fields())
        fields.extend(self.entry_type.get_optional_fields())

        for entry in fields:
            if entry[0] == key:
                if entry[1] == str:
                    return '"' + value + '"'
                return str(value)
        return ""

    def as_human_readable(self):
        ret = ""
        ret += self.get_type() + " entry: \n"
        for [key, value] in self.data.items():
            ret += key + ": " + value + "\n"

        return ret
