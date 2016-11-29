import searching_dictionary
from catalog_display import display

def search_by_author(query):
    authors = searching_dictionary.read_authors()
    results = []
    if query in authors:
        results.extend(authors[query])
        for num in results:
            display(num)

def search_by_title(query):
    titles = searching_dictionary.read_titles()
    results = []
    for key in titles:
        if query.lower() in key.lower() or query == key:
            results.extend(titles[key])
            for num in results:
                display(num)
        '''elif set(query.split())|set(key.split())==set(key.split()):
            results = titles[key]
            for num in results:
                display(num)''' #not sure if want to do that

def search_by_keyword(queries):
    keywords = searching_dictionary.read_keywords()
    results = []
    for query in queries:
        if query in keywords:
            results.extend(keywords[query])
    results = list(set(results))
    for num in results:
        display(num)

def main():
    print "Search by author, title, or keyword."
    call = ''
    while call not in ['1', '2', '3', '4']:
        call = raw_input("Enter 1 for author, 2 for title, 3 for keyword, 4 to exit: ")
    if call == '1':
        author_first = raw_input("Enter author's first name: ").strip()
        author_last = raw_input("Enter author's last name: ").strip()
        query = author_first+" "+author_last
        search = search_by_author(query)
        if search == None:
            query = author_last+", "+author_first
            search = search_by_author(query)
    elif call == '2':
        query = raw_input("Enter title: ")
    elif call == '3':
        num = int(raw_input("Number of keywords to search for: "))
        queries = []
        for i in range(num):
            queries.append(raw_input("Keyword: ").strip())
        search_by_keyword(queries)
    else:
        quit()

if __name__ == "__main__":
    main()
