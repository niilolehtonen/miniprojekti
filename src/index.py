def formatInput(inputAuthor, inputTitle, inputPublisher, inputAddress, inputYear, inputKey):
    formated = "@book{" + inputKey
    formated += ",\n  author    = \"" + inputAuthor
    formated += "\",\n  title     = \"" + inputTitle
    formated += "\",\n  publisher = \"" + inputPublisher
    formated += "\",\n  address   = \"" + inputAddress
    formated += "\",\n  year      = " + inputYear
    formated += "\n}"

    return formated


def main():
    book = """@book{CitekeyBook,
    author    = "Leonard Susskind and George Hrabovsky",
    title     = "Classical mechanics: the theoretical minimum",
    publisher = "Penguin Random House",
    address   = "New York, NY",
    year      = 2014
  }"""

    while True:
        inputString = input('What would you like to do? add/fetch/quit')
        if inputString == "add":
            inputAuthor = input("Give the name of the author: ")
            inputTitle = input("Give the book title: ")
            inputPublisher = input("Give the name of the publisher: ")
            inputAddress = input("Give the address of the publisher: ")
            inputYear = input("Give the year of the publishing: ")
            inputKey = input("Give key name to book in latex: ")

            print(formatInput(inputAuthor, inputTitle, inputPublisher, inputAddress, inputYear, inputKey))

        elif inputString == "fetch":
            break

        elif inputString == "quit":
            break


if __name__ == '__main__':
    main()
