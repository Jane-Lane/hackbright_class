'''This file reads from keywords.txt, authors.txt, titles.txt
'''
def read_keywords():
    try:
        file = open("keywords.txt", 'r')
        contents = file.read()
        file.close()
        if len(contents) > 0:
            keywords = eval(contents)
        else:
            keywords = {}
    except IOError:
        print "No file keywords.txt found, assuming keywords empty"
        keywords = {}
    empty_keys = [key for key in keywords if keywords[key] != None and len(keywords[key]) == 0]
    for key in empty_keys:
        del keywords[key]
    return keywords

def update_keywords(keywords):
    if len(keywords) != 0:
        for key in keywords:
            keywords[key] = list(set(keywords[key]))
        file = open("keywords.txt", 'w')
        file.write(str(keywords))
        file.close()

def add_keywords(more_keywords):
    keywords = read_keywords()
    for key in more_keywords:
        if key in keywords:
            keywords[key].extend(more_keywords[key])
        else:
            keywords[key] = more_keywords[key]
    update_keywords(keywords)
    return keywords

def remove_keywords(bad_keywords):
    keywords = read_keywords()
    bad_ids = []
    for key in bad_keywords:
        if key in keywords:
            if len(keywords[key]) > 0:
                print "Books %s use this keyword." % ', '.join(keywords[key])
                choice = raw_input("Would you like to remove these keywords anyway? Y/N: ").strip().lower()
                if choice == 'y':
                    bad_ids.extend(keywords[key])
                    del keywords[key]
                else:
                    print "Keyword %s not removed." % key
            else:
                del keywords[key]
                print "Keyword %s removed." % key
    update_keywords(keywords)
    return list(set(bad_ids))

def read_authors():
    try:
        file = open("authors.txt", 'r')
        contents = file.read()
        file.close()
        if len(contents) > 0:
            authors = eval(contents)
        else:
            authors = {}
    except IOError:
        print "No file authors.txt found, assuming authors empty"
        authors = {}
    empty_keys = [key for key in authors if authors[key] != None and len(authors[key]) == 0]
    for key in empty_keys:
        del authors[key]
    return authors

def update_authors(authors):
    if len(authors) != 0:
        for a in authors:
            authors[a] = list(set(authors[a])) #no repetition!
        file = open("authors.txt", 'w')
        file.write(str(authors))
        file.close()

def add_authors(more_authors):
    authors = read_authors()
    for a in more_authors:
        if a in authors:
            authors[a].extend(more_authors[a])
        else:
            authors[a] = more_authors[a]
    update_authors(authors)
    return authors

def remove_authors(bad_authors):
    authors = read_authors()
    bad_ids = []
    for a in bad_authors:
        if a in authors:
            if len(authors[a]) > 0:
                print "Books %s are by this author." % ', '.join(authors[a])
                choice = raw_input("Would you like to remove this author anyway? Y/N: ").strip().lower()
                if choice == 'y':
                    bad_ids.extend(authors[a])
                    del authors[a]
                else:
                    print "Author %s not removed." % a
            else:
                del authors[a]
                print "Author %s removed." % a
    update_authors(authors)
    return list(set(bad_ids))

def read_titles():
    try:
        file = open("titles.txt", 'r')
        contents = file.read()
        file.close()
        if len(contents) > 0:
            titles = eval(contents)
        else:
            titles = {}
    except IOError:
        print "No file titles.txt found, assuming titles empty"
        titles = {}
    empty_keys = [key for key in titles if titles[key] != None and len(titles[key]) == 0]
    for key in empty_keys:
        del titles[key]
    return titles

def update_titles(titles):
    if len(titles) != 0:
        for t in titles:
            titles[t] = list(set(titles[t]))
        file = open("titles.txt", 'w')
        file.write(str(titles))
        file.close()

def add_titles(more_titles):
    titles = read_titles()
    for t in more_titles:
        if t in titles:
            titles[t].extend(more_titles[t])
        else:
            titles[t] = more_titles[t]
    update_titles(titles)
    return titles

def remove_titles(bad_titles):
    titles = read_titles()
    bad_ids = []
    for t in bad_titles:
        if t in titles:
            if len(titles[t]) > 0:
                print "Books %s have this title." % ', '.join(titles[t])
                choice = raw_input("Would you like to remove this title anyway? Y/N: ").strip().lower()
                if choice == 'y':
                    bad_ids.extend(titles[t])
                    del titles[t]
                else:
                    print "Title %s not removed." % t
            else:
                del titles[t]
                print "Title %s removed." % t
    update_titles(titles)
    return list(set(bad_ids))

def remove_id(dictionary, book_id):
    for key in dictionary:
        while book_id in dictionary[key]:
            dictionary[key].remove(book_id)
        if len(dictionary[key])==0:
            del dictionary[key]
        return dictionary

def remove_books(ids):
    authors = read_authors()
    titles = read_titles()
    keywords = read_keywords()
    for library_id in ids:
        remove_id(authors, library_id)
        remove_id(titles, library_id)
        remove_id(keywords, library_id)
    update_titles(titles)
    update_authors(authors)
    update_keywords(keywords)

def main(): #Files will exist after the first time this is run.
    titles = read_titles()
    authors = read_authors()
    keywords = read_keywords()
    update_titles(titles)
    update_authors(authors)
    update_keywords(keywords)

if __name__ == "__main__":
    main()
