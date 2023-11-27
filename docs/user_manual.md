## User manual

### Instructions

Download the latest code from the GitHub repository by clicking 'Download ZIP' under the code section and unpack the zip-file.

### Installation

1. Install dependecies:

```
poetry install
```

2. Configure the application
* Add environment variables: ``SECRET_KEY`` 
  * Can be added as .env file using developer dependencies

3. Enter poetry shell:

```
poetry shell
```

4.Start the application:

```
python3 src/index.py
```

### Using the application



With the program, you can save bibtex with a simple form. You can retrieve saved texts from file.

First, the program will ask you what you want to do. You can answer 'add book' to add a new book entry into system. You can answer 'add manual' to add a new manual entry into system. You can answer 'fetch' to retrieve all entries in bibtex format. You can answer 'quit' to quit the program. 

When adding a new entry, the system will ask both compulsory and optional information about it. Once you have entered the information, the application will either save the details to an sql database, or ask you to re-check the input fields for correct input formats. After saving the details, you will be taken back to the main page.

When fetching the entry details, you will be shown the details from the saved entries. 



