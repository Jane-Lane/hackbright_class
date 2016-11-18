from catalog_entry import CatalogEntry
from api_attempts import get_info
from api_attempts import raw_info

file_check = raw_input("I expect a file called isbn.txt. Is there one? Y/N").strip().lower()
books = []
if file_check[0] == 'y':
    with open('isbn.txt', 'r') as file:
        for line in file:
            isbn = line.strip()
            if isbn != '':
                book = get_info(isbn)
                if book is not None:
                    print 'Adding to catalogue: %s by %s' %(book.title, book.author)
                    if book in books:
                        index = books.index(book) #need to write a function to do this
                        book = books[index]
                        book.copies += 1
                        books[index] = book
                    else:
                        books.append(book)
        
else:
    entry = raw_input("Press 1 to enter an ISBN, 2 to name another file, anything else to exit:")
    if entry == '1':
        isbn = raw_input("ISBN: ")
    elif entry == '2':
        file_name = raw_input("File name: ").strip()
        with open(file_name, 'r') as file:
            for line in file:
                isbn = line.strip()
                if isbn != '':
                    book = get_info(isbn)
                    if book is not None:
                        print 'Adding to catalogue:', book
                        if book in books:
                            index = books.index(book)
                            book = books[index]
                            book.copies += 1
                            books[index] = book
                        else:
                            books.append(book)

with open("catalogue.txt", 'a') as catalog:
    for book in books:
        catalog.write(str(book))
