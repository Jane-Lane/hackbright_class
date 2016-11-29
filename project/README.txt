This project involves making a library catalogue.

Right now it’s very basic.  To test out what I’ve been doing, modify the file isbn.txt to take a list of ISBNs, or make your own file, and run the script basic_entries.py.  Then look at the files titles.txt, authors.txt, keywords.txt to see searchable terms, or run search_ui.py.  

Each record will be stored as a file "N.txt" where "N" is a library ID number; the file id_index.txt tracks used ID numbers.  Warning: if you keep running basic_entries.py then records will be copied multiple times with multiple IDs.

The script catalog_entry.py defines a Python class called Record, and another class CatalogEntry that inherits from this.  It is still pretty buggy, but the Record class is meant for the library's record which gives each book a distinct ID number, and the CatalogEntry class is meant for the UI.

The script api_attempts.py takes in ISBN numbers, strips out non-numeric characters, and pulls info from the Open Library website.

The file isbn.txt is a sample list of ISBNs, each one on a new line.