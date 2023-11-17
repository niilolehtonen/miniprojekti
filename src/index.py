from entities.book import Book
from services.file_saver import FileSaver
from services.file_fetcher import FileFetcher

def main():
    while True:
        input_string = input('What would you like to do? add/fetch/quit: ')
        if input_string == "add":
            input_author = input("Give the name of the author: ")
            input_title = input("Give the book title: ")
            input_publisher = input("Give the name of the publisher: ")
            input_address = input("Give the address of the publisher: ")
            input_year = int(input("Give the year of the publishing: "))
            input_key = input("Give key name to book in latex: ")

            book = Book(input_author, input_title, input_publisher, input_address, input_year, input_key)

            file_saver = FileSaver("data.bib")
            file_saver.save(book)

        elif input_string == "fetch":
            file_fetcher = FileFetcher()
            print(file_fetcher.fetch())

        elif input_string == "quit":
            break


if __name__ == '__main__':
    main()
