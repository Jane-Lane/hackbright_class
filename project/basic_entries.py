from catalog_entry import CatalogEntry
from api_attempts import get_info
from api_attempts import raw_info

import searching_dictionary
PATH = "plaintext_files/"

file_check = raw_input("I expect a file called isbn.txt. Is there one? Y/N").strip().lower()
books = []
isbn_list = []
if file_check[0] == 'y':
    with open('isbn.txt', 'r') as file:
        for line in file:
            isbn = line.strip()
            isbn_list.append(isbn)
            if isbn != '':
                book = get_info(isbn)
                if book is not None:
                    print 'Adding to catalogue: %s by %s' %(book.title, book.author)
                    books.append(book)
    with open('isbn.txt', 'w') as file: #clear ISBNs
        file.write('')        
else:
    entry = raw_input("Press 1 to enter an ISBN, 2 to name another file, anything else to exit:")
    if entry == '1':
        isbn = raw_input("ISBN: ").strip()
        isbn_list.append(isbn)
    elif entry == '2':
        file_name = raw_input("File name: ").strip()
        with open(file_name, 'r') as file:
            for line in file:
                isbn = line.strip()
                isbn_list.append(isbn)
                if isbn != '':
                    book = get_info(isbn)
                    if book is not None:
                        print 'Adding to catalogue:', book
                        books.append(book)
        with open(file_name, 'w') as file: #clear the file
            file.write('')

with open(PATH+"all_isbns.txt", 'a') as outfile: #dump ISBNS into file
    for isbn in isbn_list:
        outfile.write(isbn)
        outfile.write('\n')

used_ids = []
with open("id_index.txt", 'r') as file:
    for line in file:
        used_ids.append(int(line))

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

with open("id_index.txt", 'w') as file:
    for num in all_ids:
        file.write(str(num))
        file.write("\n")

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
    file_name = PATH + book.library_id+".txt"
    with open(file_name, 'w') as file:
        file.write(str(book))
