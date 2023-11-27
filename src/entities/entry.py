class Entry:
    def __init__(self, input_data: dict, entry_type, keygen):
        self.entryType = entry_type
        self.data = {}
        self.keygen = keygen
        for requiredField in entry_type.get_required_fields():
            if requiredField[0] not in input_data.keys():
                raise requiredField[0] + "not found"
            self.data[requiredField[0]] = input_data[requiredField[0]]

        for optionalField in entry_type.get_optional_fields():
            if optionalField[0] in input_data.keys() and input_data[optionalField[0]] != "":
                print(optionalField)
                self.data[optionalField[0]] = input_data[optionalField[0]]

    def get_type(self):
        return self.entryType.get_type()

    def format(self):
        formatted = "@" + self.get_type() + "{" + self.keygen.generate_key(self.data["title"]) + ",\n"
        items = list(self.data.items())
        for i in range(len(items) - 1):
            item = items[i]
            formatted += item[0] + "\t=" + str(item[1]) + ",\n"
        formatted += items[-1][0] + "\t=" + str(items[-1][1]) + "\n"
        formatted += "}"
        return formatted
