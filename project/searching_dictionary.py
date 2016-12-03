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
    return keywords

def update_keywords(keywords):
    if len(keywords) != 0:
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
    return authors

def update_authors(authors):
    if len(authors) != 0:
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
    return titles

def update_titles(titles):
    if len(titles) != 0:
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

def main(): #Files will exist after the first time this is run.
    titles = read_titles()
    authors = read_authors()
    keywords = read_keywords()
    update_titles(titles)
    update_authors(authors)
    update_keywords(keywords)

if __name__ == "__main__":
    main()



##    with open("keywords.txt", 'r') as file:
##        for line in file:
##            line = line.strip()
##            if len(line) > 0:
##                line = line.split(":")
##                key = line[0]
##                if key in keywords:
##                    print "Error: repeated keyword %s, merging" % key
##                else:
##                    keywords[key] = []
##                try:
##                    values = line[1].split()
##                    keywords[key].extend(values)
##                except IndexError:
##                    print "No records for keyword %s, removing" % key
##                if len(keywords[key])==0:
##                    del keywords[key]
##    return keywords

    ##def read_authors():
##    authors = {}
##    with open("authors.txt", 'r') as file:
##        for line in file:
##            line = line.strip()
##            if len(line) > 0:
##                line = line.split(":")
##                key = line[0]
##                if key in authors:
##                    print "Error: repeated author %s, merging" % key
##                else:
##                    authors[key] = []
##                try:
##                    values = line[1].split()
##                    authors[key].extend(values)
##                except IndexError:
##                    print "No records for author %s, removing" % key
##                if len(authors[key])==0:
##                    del authors[key]
##    return authors
##
##def read_titles():
##    titles = {}
##    with open("titles.txt", 'r') as file:
##        for line in file:
##            line = line.strip()
##            if len(line) > 0:
##                line = line.split(":")
##                key = line[0]
##                if key in titles:
##                    print "Error: repeated title %s, merging" % key
##                else:
##                    titles[key] = []
##                try:
##                    values = line[1].split()
##                    titles[key].extend(values)
##                except IndexError:
##                    print "No records for title %s, removing" % key
##                if len(titles[key])==0:
##                    del titles[key]
##    return titles
##
##def update_titles(titles):
##    with open("titles.txt", 'w') as file:
##        for key in titles:
##            file.write(key)
##            file.write(":")
##            for num in titles[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')
##
##def add_titles(titles):
##    with open("titles.txt", "a") as file:
##        for key in titles:
##            file.write(key)
##            file.write(":")
##            for num in titles[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')
##
##def update_authors(authors):
##    with open("authors.txt", 'w') as file:
##        for key in authors:
##            file.write(key)
##            file.write(":")
##            for num in authors[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')
##
##def add_authors(authors):
##    with open("authors.txt", 'a') as file:
##        for key in authors:
##            file.write(key)
##            file.write(":")
##            for num in authors[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')
##
##def update_keywords(keywords):
##    with open("keywords.txt", 'w') as file:
##        for key in keywords:
##            file.write(key)
##            file.write(":")
##            for num in keywords[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')
##
##def add_keywords(keywords):
##    with open("keywords.txt", 'a') as file:
##        for key in keywords:
##            file.write(key)
##            file.write(":")
##            for num in keywords[key]:
##                file.write(num)
##                file.write(' ')
##            file.write('\n')

