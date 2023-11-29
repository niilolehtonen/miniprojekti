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
4. Initialize the database:

```
python3 src/initialize_database.py
```

5. Start the application:

```
python3 src/index.py
```

6. Open the application web page in a browser

### Using the application



With the program, you can save bibtex with a simple form. You can download saved texts as a bibtex file or view them in a browser.

On the main page, you can select what you want to do. You can click the links of book creation, manual creation, viewing all added entries or downloading all entries as a bibtex file.

When adding a new entry, the system will ask both compulsory and optional information about it. Once you have entered the information, the application will either save the details to an sql database, or ask you to re-check the input fields for correct input formats. After saving the details, you will be taken back to the main page.

When fetching the entry details by pressing "See all references", you will be shown the details from the saved entries as a human-readable form.

You can download the references in bibtex format by pressing the "Download all references" button.



