This project involves making a library catalogue.

Right now it’s very basic.  To test out what I’ve been doing, modify the file isbn.txt to take a list of ISBNs, or make your own file, and run the script basic_entries.py.

The script catalog_entry.py defines a Python class called CatalogEntry.  It can hold a lot of information but currently only displays title, author, publisher, and ISBN.  I’m having a little trouble managing how to deal with equivalence of books given two different ISBN formats.

The script api_attempts.py takes in ISBN numbers, strips out non-numeric characters, and pulls info from the Open Library website.

The file isbn.txt is a sample list of ISBNs, each one on a new line.

The script basic_entries.py reads the file isbn.txt and writes to a file called catalogue.txt, ignoring any books for which it cannot find info.  Right now, if the catalogue already exists it writes to the end; it does not currently load from the catalogue as I need to decide how to store more complete catalogue entries.