from basic_entries import PATH
import os
import searching_dictionary
from catalog_entry import *

ids = []

def make_id_list():
    all_files = next(os.walk(PATH))[2]
    existing_records = [x.strip('.txt') for x in all_files if x[0] in '0123456789']
    return map(int, existing_records)

try:
    with open(PATH+"id_index.txt", 'r') as file:
        contents = file.read().strip()
        if len(contents) > 0:
            try:
                ids = eval(contents)
            except SyntaxError:
                ids = contents.split()
except IOError:
    print "Missing id_index.txt file, I'll make one from existing records"
    all_records = sorted(make_id_list())
    with open(PATH+"id_index.txt", 'w') as file:
        file.write(str(all_records))

def update_search_terms(ids):
    keywords = searching_dictionary.read_keywords()
    authors = searching_dictionary.read_authors()
    titles = searching_dictionary.read_titles()
    for key in keywords:
        keywords[key] = list(set([x for x in keywords[key] if x in ids]))
    searching_dictionary.update_keywords(keywords)
    for a in authors:
        authors[a] = list(set([x for x in authors[a] if x in ids]))
    searching_dictionary.update_authors(authors)
    for t in titles:
        titles[t] = list(set([x for x in titles[t] if x in ids]))
    searching_dictionary.update_titles(titles)

def fix_search_files():
    global ids
    ids.extend(make_id_list())
    keywords = {}
    titles = {}
    authors = {}
    for library_id in ids:
        with open(PATH+str(library_id)+".txt", 'r') as file:
            contents = file.read()
            if len(contents) > 0:
                book = record_from_string(contents)
                author = book.author
                title = book.title
                keys = book.keywords
                if author not in authors:
                    authors[author] = []
                authors[author].append(library_id)
                if title not in titles:
                    titles[title] = []
                titles[title].append(library_id)
                for word in keys:
                    if word not in keywords:
                        keywords[word] = []
                    keywords[word].append(library_id)
            else:
                print "Error: record %s empty. Please remove manually or fix it." % library_id
    searching_dictionary.add_authors(authors)
    searching_dictionary.add_titles(titles)
    searching_dictionary.add_keywords(keywords)

def main():
    global ids
    real_ids = make_id_list()
    false_ids = [x for x in ids if x not in real_ids]
    unlisted_ids = [x for x in real_ids if x not in ids]
    print "Bad IDs found:", str(false_ids)[1:-1]
    print "%i total records found" % len(real_ids)
    print "Unlisted records: %s" % str(unlisted_ids)[1:-1]
    if len(false_ids) > 0:
        if raw_input("Delete bad IDs? Y/N").strip().lower()== 'y':
            ids = real_ids
            print "Okay, only good IDs included now."
        else:
            ids = real_ids+false_ids
            ids.sort()
    else:
        ids = real_ids
        ids.sort()
    with open(PATH+"id_index.txt", 'w') as file:
        file.write(str(ids))      
    update_search_terms(ids)
    fix_search_files()

if __name__ == "__main__":
    main()
