#-*- coding: UTF-8 -*-
from urllib2 import urlopen
import json
from catalog_entry import Record

def example_isbns():
    examples = {}
    examples['fledgling'] = "9780446696166"
    examples['fledgling_10'] = "0446696161"
    examples['everfair'] = "9780765338051"
    examples['inconvenient_indian'] = "9780816689767"
    examples['crescent_moon'] = "978-0-7564-0711-7"
    examples['the_root'] = "9781597808637"
    examples['fifth_season'] = "9780316229296"
    return examples
    
def strip_isbn(isbn): #takes out non-numeric characters
    digits = [x for x in isbn if x in '0123456789']
    isbn = ''.join(digits)
    return isbn

first_url = "http://openlibrary.org/api/books?bibkeys="
third_url = "&format=json&jscmd=data"

def raw_info(isbn):
    key = 'ISBN:'+strip_isbn(isbn)
    link = first_url+key+third_url
    request = urlopen(link) #What if this breaks??? Fix
    data = json.load(request)
    return data

def get_info(isbn):
    key = 'ISBN:'+strip_isbn(isbn)
    data = raw_info(isbn)
    if len(data) == 0:
        print "No Open Library info found for", key
        return None
    elif key in data and len(data.keys())==1:
        data = data[key]
    else:
        print "Unexpectedly too much data found for", key
        print "Start of raw data:"
        print str(data)[0:40]
        return None #hacky just fix this later too
    title = data['title'].encode('utf-8')
    author = data['authors'][0]['name'].encode('utf-8')
    subjects = []
    publishers = []
    if 'subjects' in data:
        for x in data['subjects']:
            if 'DAISY' not in x['name'] and x['name']!= 'OverDrive':
                subjects.append(x['name'].encode('utf-8'))
    #else:
    #    print "No subjects found"
    if 'publishers' in data:
        publishers = [x['name'].encode('utf-8') for x in data['publishers']]
    ret = Record(ISBN=isbn, title=title, author=author)
    ret.publisher = publishers[0]
    ret.all_authors = [x['name'].encode('utf-8') for x in data['authors']]
    ret.keywords = subjects
    return ret
