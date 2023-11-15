def format_input(input_author, input_title, input_publisher, input_address, input_year, input_key):
    formated = "@book{" + input_key
    formated += ",\n  author    = \"" + input_author
    formated += "\",\n  title     = \"" + input_title
    formated += "\",\n  publisher = \"" + input_publisher
    formated += "\",\n  address   = \"" + input_address
    formated += "\",\n  year      = " + input_year
    formated += "\n}"

    return formated


def main():
    while True:
        input_string = input('What would you like to do? add/fetch/quit')
        if input_string == "add":
            input_author = input("Give the name of the author: ")
            input_title = input("Give the book title: ")
            input_publisher = input("Give the name of the publisher: ")
            input_address = input("Give the address of the publisher: ")
            input_year = input("Give the year of the publishing: ")
            input_key = input("Give key name to book in latex: ")

            print(format_input(input_author, input_title, input_publisher, input_address, input_year, input_key))

        elif input_string == "fetch":
            break

        elif input_string == "quit":
            break


if __name__ == '__main__':
    main()
