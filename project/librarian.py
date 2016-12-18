import inspect
import basic_entries
from basic_entries import PATH
import searching_dictionary
import search_ui
from catalog_entry import *

record_list = []
manual_books = []
to_remove = []
titles = searching_dictionary.read_titles()
authors = searching_dictionary.read_authors()
keywords = searching_dictionary.read_keywords()

def make_list():
    global record_list
    print '''Let's search for records to add to your list.
Enter 'title' to search for records by title, and 'ID' to search for records by ID.'''
    choice = raw_input().strip().lower()
    if choice == 'title':
        if raw_input("Enter 'all' to display all titles: ").strip().lower() != 'all':
            start_string = raw_input("Show titles in alphabetical order from: ").strip().lower()
            stop_string = raw_input("Show titles in alphabetical order up to: ").strip().lower()
            results = display_by_title(start_string, stop_string)
        else:
            results = display_by_title('!', None)
    elif choice == 'id':
        print "Write 'from [ID] to [ID]' to get all IDs in that range, or write a list of IDs separated by commas and/or spaces."
        input_string = raw_input("IDs to manage: ").strip().lower()
        if input_string[0] == 'f':
            four_things = input_string.split()
            start = int(four_things[1])
            stop = int(four_things[3])+1
            results = map(str, list(range(start, stop)))
        else:
            spaced_string = input_string.replace(',', ' ')
            results = spaced_string.split()
    else:
        results = []
        return None
    print "Which of these would you like to manage?"
    requests = raw_input("Type 'all', 'none', or a list of library IDs separated by commas or spaces: ").strip().lower()
    if requests == 'all':
        record_list.extend(results)
    elif requests == 'none':
        pass
    else:
        requests = requests.replace(',', ' ')
        record_list.extend(requests.split())

def manage_book(id_number):
    id_number = int(id_number)
    print "Managing library ID %i" %id_number
    try:
        file = open(PATH+str(id_number)+'.txt', 'r')
        contents = file.read()
        book = record_from_string(contents)
        file.close()
    except IOError:
        print "Oops, no record found. Skipping this one."
        return
    print book
    choice = raw_input("To remove this book, type 'remove' or 'r'. To edit, type 'edit'. To add another copy, type 'copy'. ").strip().lower()
    if choice == 'remove' or choice == 'r':
        to_remove.append(id_number) #Will run after all books are managed
        basic_entries.remove_book(id_number)
    elif choice == 'edit':
        file = open(PATH+str(id_number)+'.txt', 'w')
        while(True):
            print "Press enter to stop editing."
            attr = raw_input("Which would you like to edit? Title, ISBN, LCCN, author, publisher, or keywords: ").strip().lower()
            if attr == 'title':
                book.title = raw_input("New title: ").strip()
                print book
            elif attr == 'author':
                book.author = raw_input("New author: ").strip()
                print book
            elif attr == 'isbn':
                book.isbn = basic_entries.strip_isbn(raw_input("New ISBN: ").strip())
                print book
            elif attr == 'lccn':
                book.lccn = raw_input("New LCCN: ").strip()
                print book
            elif attr == 'publisher':
                book.publisher = raw_input("New publisher: ").strip()
            elif attr == 'keywords':
                new_keyword_string = raw_input("Enter additional keywords separated by commas: ").strip()
                new_keywords = map(lambda x: x.strip(), new_keyword_string.split(','))
                if len(book.keywords) > 0:
                    while '' in book.keywords:
                        book.keywords.remove('')
                    deletion = raw_input("Enter 'delete' to delete old keywords, or a specific keyword to delete it: ").strip()
                    if deletion.lower() == 'delete':
                        book.keywords = new_keywords
                    elif deletion != '' and deletion in book.keywords:
                        book.keywords.remove(deletion)
                        book.keywords.extend(new_keywords)
                    else:
                        book.keywords.extend(new_keywords)
                else:
                    book.keywords = new_keywords
                print book
            elif attr == 'library_id':
                print "To change the library ID, please copy the book to a new ID and remove this copy."
            else:
                break
        file.write(str(book))
        file.close()
    elif choice == 'copy':
        pass

def display_by_title(start_string, stop_string): #inclusive on both ends
    start_string = start_string.lower()
    if stop_string is not None:
        stop_string = stop_string.lower()+'z'*50
    titles_list = titles.keys()
    titles_list.sort()
    titles_lowercase = map(str.lower, titles_list)
    num = len(titles_lowercase)
    start_index = 0
    while start_index < num and titles_lowercase[start_index] < start_string:
        start_index += 1
    if stop_string is None:
        stop_index = num
    else:
        stop_index = start_index
        while stop_index < num and titles_lowercase[stop_index] <= stop_string: 
            stop_index += 1
    selected = titles_list[start_index: stop_index]
    results = []
    for title in selected:
        results.extend(titles[title])
        print title[0:30], ": Library ID", str(titles[title])[1:-1]
    return results

def display_by_id(start_index, stop_index):
    results = []
    for id_number in range(start_index, stop_index + 1):
        try:
            with open(PATH+str(id_number)+'.txt') as file:
                book = record_from_string(file.read())
            results.append(book.title())
        except IOError:
            error_count += 1
            print "No record found for Library ID %s" %id_number
        if error_count >= 20:
            override = raw_input("At least 20 records not found. Keep going? Y/N").strip().lower()
            if override != 'y':
                break
        if error_count >= 100:
            override = raw_input("At least 100 records not found. Keep going? Y/N").strip().lower()
            if override != 'y':
                break
    return results

def manual_entry(isbn):
    global manual_books
    print "Manual entry for ISBN %s" % isbn
    title = raw_input("Enter title: ").strip()
    author = raw_input("Enter author: ").strip()
    publisher = raw_input("Enter publisher: ").strip()
    keywords = []
    while(True):
        word = raw_input("Enter a keyword, or 'none' to stop entering keywords: ").strip()
        if word.lower() != 'none':
            keywords.append(word)
        else:
            break
    book = Record(ISBN=isbn)
    book.title = title
    book.author = author
    book.publisher = publisher
    book.keywords = keywords
    manual_books.append(book)
    

def display_menu():
    print '''Main menu:
Type "0" or "menu" to display this menu again.
Type "1" or "manage" to edit, delete, or manually add records.
Type "2" or "update" to run the inspection script, which will update the list
of used library IDs to reflect the current records in the catalogue.
Type "3", "add books", or "ISBN" to add a list of books to the catalogue by ISBN.
Type "4" or "exit" to exit the program.
'''

def main():
    global to_remove
    print "Welcome to Elizabeth's Library Catalog Software!"
    display_menu()
    while(True):
        choice = raw_input("Please choose an option, use 'menu' to display options: ").strip().lower()
        if choice == '4' or choice == 'exit':
            break
        elif choice == '0' or choice == 'menu':
            display_menu()
        elif choice == '1' or choice == 'manage':
            make_list()
            while len(record_list) > 0:
                manage_book(record_list.pop())
            searching_dictionary.remove_books(to_remove) #after managing has been done
            display_menu()
        elif choice == '2' or choice == 'update':
            inspect.main()
        elif choice == '3' or choice == 'add books' or choice == 'isbn':
            basic_entries.main()
            with open('not_found_isbns.txt', 'r') as file:
                how_many = len(file.readlines())
                if how_many > 0:
                    print "There are %s ISBNs that could not be found automatically." % how_many
                    choice2  = raw_input("Would you like to enter their information manually? Y/N: ").strip().lower()
                    if choice2 == 'y':
                        file.seek(0)
                        for line in file:
                            isbn = basic_entries.strip_isbn(line)
                            manual_entry(isbn)
                        basic_entries.main(manual_books)
        else: #wrong choices
            display_menu()

if __name__ == "__main__":
    main()
