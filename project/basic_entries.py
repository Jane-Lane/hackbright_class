from catalog_entry import *
from api_attempts import get_info
from api_attempts import raw_info
import os
import searching_dictionary
PATH = "do_not_change/"

if not os.path.isdir(PATH[0:-1]):
    os.makedirs(PATH[0:-1])
books = []
isbn_list = []
not_found = []

def add_book(isbn):
    if isbn != '':
        book = get_info(isbn)
        if book is not None:
            print 'Adding to catalogue: %s by %s' %(book.title[0:30], book.author)
            books.append(book)
            return book
        else:
            not_found.append(isbn)

def remove_book(id_number):
    try:
        os.remove(PATH+str(id_number)+'.txt')
        print "Record %s.txt removed. Remember to run the update script when you're done."%(id_number)
    except OSError:
        pass
    
def main(extra_books = None):
    print "By default, I read a list of ISBNs off of isbn.txt, one per line."
    file_check = raw_input("Would you like to read a list of ISBNs from isbn.txt? Y/N: ").strip().lower()
    global books
    if extra_books is not None:
        books.extend(extra_books)
    global isbn_list
    global not_found
    if file_check[0] == 'y':
        with open('isbn.txt', 'r') as file:
            for line in file:
                isbn = line.strip()
                isbn_list.append(isbn)
                if isbn != '':
                    add_book(isbn)
        with open('isbn.txt', 'w') as file: #clear ISBNs
            file.write('')       
    else:
        entry = raw_input("Press 1 to enter an ISBN, 2 to name another file, anything else to exit:")
        if entry == '1':
            while(True):
                print "Enter an ISBN number, or 'exit' to exit."
                isbn = raw_input("ISBN: ").strip().lower()
                if isbn != '' and isbn != 'exit':
                    isbn_list.append(isbn)
                    add_book(isbn)
                elif isbn == 'exit':
                    break
                else:
                    print "No ISBN entered, please try again."
        elif entry == '2':
            file_name = raw_input("File name: ").strip()
            with open(file_name, 'r') as file:
                for line in file:
                    isbn = line.strip()
                    isbn_list.append(isbn)
                    if isbn != '':
                        add_book(isbn)
            with open(file_name, 'w') as file: #clear the file
                file.write('')

    with open(PATH+"all_isbns.txt", 'a') as outfile: #dump ISBNS into file
        for isbn in isbn_list:
            outfile.write(strip_isbn(isbn))
            outfile.write('\n')
    with open("not_found_isbns.txt", 'a') as outfile:
        for isbn in not_found:
            outfile.write(strip_isbn(isbn))
            outfile.write('\n')

    used_ids = []
    try:
        with open(PATH+"id_index.txt", 'r') as file:
            contents = file.read()
        if len(contents) > 0:
            used_ids = eval(contents)
            used_ids = map(int, used_ids)
    except IOError:
        last = 0

    if len(used_ids) == 0:
        last = 0
    else:
        last = max(used_ids)
    recycle_ids = [x for x in range(last) if x not in used_ids]
    new_ids = []
    for i in range(len(books)):
        if i < len(recycle_ids):
            new_ids.append(recycle_ids[i])
        else:
            new_ids.append(i + last + 1 - len(recycle_ids))

    all_ids = used_ids + new_ids
    if len(all_ids) > 0:
        all_ids.sort()

    with open(PATH+"id_index.txt", 'w') as file:
        file.write(str(all_ids))

    keywords = {}
    titles = {}
    authors = {}
    for i in range(len(new_ids)):
        id_num = str(new_ids[i])
        books[i].library_id = id_num
        author = books[i].author
        title = books[i].title
        keys = books[i].keywords
        if author not in authors:
            authors[author] = []
        authors[author].append(id_num)
        if title not in titles:
            titles[title] = []
        titles[title].append(id_num)
        for word in keys:
            if word not in keywords:
                keywords[word] = []
            keywords[word].append(id_num)

    searching_dictionary.add_authors(authors)
    searching_dictionary.add_titles(titles)
    searching_dictionary.add_keywords(keywords)

    for book in books:
        file_name = PATH + str(book.library_id)+".txt"
        with open(file_name, 'w') as file:
            file.write(str(book))

if __name__ == "__main__":
    main()
