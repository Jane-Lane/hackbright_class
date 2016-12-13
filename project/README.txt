This project involves making a library catalogue.

Right now it’s very basic.  To test out what I’ve been doing, modify the file isbn.txt to take a list of ISBNs, on on each line, and run the script librarian.py.  (It also allows you to name a different file of ISBNs, or enter them manually.)  

The script creates a folder do_not_change/ which holds all current records, a backup file of all previously entered ISBNs, and a file listing the currently used IDs.  The folder should be handled by the script rather than changed manually.

Each record will be stored as a file "N.txt" where "N" is a library ID number; the file id_index.txt tracks used ID numbers.  Warning: if you keep running basic_entries.py then records will be copied multiple times with multiple IDs.

The librarian.py script relies on the following:

The file catalog_entry.py defines a Python class called Record, with bibliographic entries as attributes.

The file api_attempts.py takes in ISBN numbers, strips out non-numeric characters, and pulls info from the Open Library website.

The file basic_entries.py uses the above two scripts, takes in ISBN

The file isbn.txt is a sample list of ISBNs, each one on a new line.  The file not_found.txt stores ISBNs which cannot be found on the Open Library database, for the librarian to enter manually.  (This part of the script is problematic right now)

The files keywords.txt, authors.txt and titles.txt keep track of library IDs by keyword, author and title respectively; the file searching_dictionary.py loads these files and allows a search by title, author or keyword.

Other files and folders are not currently used; eventually I want to download MARC files in addition to writing plaintext files.