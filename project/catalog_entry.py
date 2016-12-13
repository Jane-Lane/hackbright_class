def strip_isbn(isbn): #takes out non-numeric characters
    digits = [x for x in isbn if x in '0123456789']
    isbn = ''.join(digits)
    return isbn

class Record(object):
    def __init__(self, library_id = '', ISBN = '', title='', author=''):
        self.library_id = library_id
        isbn = strip_isbn(ISBN)
        if len(isbn) == 13:
            self.isbn_13 = isbn
            self.isbn = isbn
            self.isbn_10 = isbn[3:]
        elif len(isbn) == 10:
            self.isbn_10 = isbn
            self.isbn_13 = '978'+isbn
            self.isbn = self.isbn_13
        elif len(isbn) == 9:
            self.isbn_10 = '0'+isbn
            self.isbn_13 = '9780'+isbn
            self.isbn = self.isbn_13
        else:
            self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = ''
        self.all_authors = []
        self.subjects = []
        self.keywords=[]
        self.all_publishers = []
        self.lccn = ''
    def __repr__(self):
        s = '''
Title: %s
Author: %s
Publisher: %s
ISBN: %s
Library of Congress catalog number: %s
Library ID: %s
Keywords: %s
'''%(self.title, self.author, self.publisher, self.isbn, self.lccn, self.library_id, ', '.join(self.keywords))
        return s

    def __eq__(self, other):
        if self.library_id == other.library_id:
            return True
        else:
            return False
    def fix_isbn(self):
        if len(self.isbn) == 13:
            self.isbn_13 = self.isbn
        elif len(self.isbn) == 10:
            self.isbn_10 = self.isbn
            self.isbn_13 = '978'+self.isbn_10
            self.isbn = self.isbn_13
        elif len(self.isbn) == 9:
            self.isbn_10 = '0'+self.isbn
            self.isbn_13 = '978'+self.isbn_10
            self.isbn = self.isbn_13
        else:
            print "Bad ISBN: %s for library ID %s" % self.isbn, self.library_id

def record_from_string(record_string):
    lines = record_string.split('\n')
    ret = Record('')
    for line in lines:
        line = line.strip()
        if line[0:6].lower() == 'title:':
            ret.title = line[6:].strip()
        if line[0:7].lower() == 'author:':
            ret.author = line[7:].strip()
        if line[0:10].lower() == 'publisher:':
            ret.publisher = line[10:].strip()
        if line[0:5].upper() == 'ISBN:':
            ret.isbn = strip_isbn(line[5:])
            ret.fix_isbn()
        if line[0:9].lower() == 'keywords:':
            ret.keywords = line[9:].split(', ')
        if line[0:11].lower() == 'library id:':
            ret.library_id = line[11:].strip()
    return ret
