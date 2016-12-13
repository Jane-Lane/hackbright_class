import inspect
import basic_entries
import searching_dictionary
import search_ui
from catalog_entry import Record

record_list = []
manual_books = []
titles = searching_dictionary.read_titles()

authors = searching_dictionary.read_authors()

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
    print "Managing library ID %s" %id_number
    choice = raw_input("To remove this book, type 'remove' or 'r'. To edit, type 'edit'. To add another copy, type 'copy'.").strip().lower()
    if choice == 'remove':
        basic_entries.remove_book(id_number)
    elif choice == 'edit':
        pass
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
        print title[0:30], ": Library ID", ', '.join(x for x in titles[title])
    return results

def display_by_id(start_index, stop_index):
    results = []
    for id_number in range(start_index, stop_index + 1):
        try:
            display(str(id_number))
            results.append(str(id_number))
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
            display_menu()
        elif choice == '2' or choice == 'update':
            inspect.main()
        elif choice == '3' or choice == 'add books' or choice == 'isbn':
            basic_entries.main()
            with open('not_found_isbns.txt', 'r') as file:
                for line in file:
                    isbn = basic_entries.strip_isbn(line)
                    manual_entry(isbn)
                basic_entries.main(manual_books)
            
        else:
            pass

if __name__ == "__main__":
    main()
