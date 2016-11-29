'''This file reads from keywords.txt, authors.txt, titles.txt
'''
def read_keywords():
    keywords = {}
    with open("keywords.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                line = line.split(":")
                key = line[0]
                if key in keywords:
                    print "Error: repeated keyword %s, merging" % key
                else:
                    keywords[key] = []
                try:
                    values = line[1].split()
                    keywords[key].extend(values)
                except IndexError:
                    print "No records for keyword %s, removing" % key
                if len(keywords[key])==0:
                    del keywords[key]
    return keywords

def read_authors():
    authors = {}
    with open("authors.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                line = line.split(":")
                key = line[0]
                if key in authors:
                    print "Error: repeated author %s, merging" % key
                else:
                    authors[key] = []
                try:
                    values = line[1].split()
                    authors[key].extend(values)
                except IndexError:
                    print "No records for author %s, removing" % key
                if len(authors[key])==0:
                    del authors[key]
    return authors

def read_titles():
    titles = {}
    with open("titles.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                line = line.split(":")
                key = line[0]
                if key in titles:
                    print "Error: repeated title %s, merging" % key
                else:
                    titles[key] = []
                try:
                    values = line[1].split()
                    titles[key].extend(values)
                except IndexError:
                    print "No records for title %s, removing" % key
                if len(titles[key])==0:
                    del titles[key]
    return titles

def update_titles(titles):
    with open("titles.txt", 'w') as file:
        for key in titles:
            file.write(key)
            file.write(":")
            for num in titles[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def add_titles(titles):
    with open("titles.txt", "a") as file:
        for key in titles:
            file.write(key)
            file.write(":")
            for num in titles[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def update_authors(authors):
    with open("authors.txt", 'w') as file:
        for key in authors:
            file.write(key)
            file.write(":")
            for num in authors[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def add_authors(authors):
    with open("authors.txt", 'a') as file:
        for key in authors:
            file.write(key)
            file.write(":")
            for num in authors[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def update_keywords(keywords):
    with open("keywords.txt", 'w') as file:
        for key in keywords:
            file.write(key)
            file.write(":")
            for num in keywords[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def add_keywords(keywords):
    with open("keywords.txt", 'a') as file:
        for key in keywords:
            file.write(key)
            file.write(":")
            for num in keywords[key]:
                file.write(num)
                file.write(' ')
            file.write('\n')

def main(): #Files will exist after the first time this is run.
    try:
        titles = read_titles()
    except IOError:
        titles = {}
    update_titles(titles)
    try:
        authors = read_authors()
    except IOError:
        authors = {}
    update_authors(authors)
    try:
        keywords = read_keywords()
    except IOError:
        keywords = {}
    update_keywords(keywords)

if __name__ == "__main__":
    main()
