from basic_entries import PATH
from os import walk
import searching_dictionary

ids = []

def make_id_list():
    all_files = next(walk(PATH))[2]
    existing_records = [x.strip('.txt') for x in all_files if x[0] in '0123456789']
    return existing_records

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
    all_records = make_id_list()
    with open(PATH+"id_index.txt", 'w') as file:
        file.write(str(all_records))


def update_search_terms():
    keywords = searching_dictionary.read_keywords()
    authors = searching_dictionary.read_authors()
    titles = searching_dictionary.read_titles()
    for key in keywords:
        keywords[key] = [x for x in keywords[key] if x in ids]
    searching_dictionary.update_keywords(keywords)
    for a in authors:
        authors[a] = [x for x in authors[a] if x in ids]
    searching_dictionary.update_authors(authors)
    for t in titles:
        titles[t] = [x for x in titles[t] if x in ids]
    searching_dictionary.update_titles(titles)

def main():
    global ids
    real_ids = make_id_list()
    false_ids = [x for x in ids if x not in real_ids]
    unlisted_ids = [x for x in real_ids if x not in ids]
    print "Bad IDs found: %s" % ', '.join(false_ids)
    print "%i total records found" % len(real_ids)
    print "Unlisted records: %s" % ', '.join(unlisted_ids)
    if len(false_ids) > 0:
        if raw_input("Delete bad IDs? Y/N").strip().lower()== 'y':
            ids = real_ids
            print "Okay, only good IDs included now."
        else:
            ids = real_ids+false_ids
            ids.sort()
    with open(PATH+"id_index.txt", 'w') as file:
        file.write(str(ids))      
    update_search_terms()

if __name__ == "__main__":
    main()
