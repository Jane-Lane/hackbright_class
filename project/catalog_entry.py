def strip_isbn(isbn): #takes out non-numeric characters
    digits = [x for x in isbn if x in '0123456789']
    isbn = ''.join(digits)
    return isbn

class Record(object):
    def __init__(self, library_id = '', ISBN = '', title='', author=''):
        self.library_id = library_id
        isbn = strip_isbn(ISBN)
        self.isbn_10 = ''
        self.isbn_13 = ''
        if len(isbn) == 13:
            self.isbn_13 = isbn
            self.isbn = isbn
        elif len(isbn) == 10:
            self.isbn_10 = isbn
            self.isbn = isbn
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
ISBN 10: %s
ISBN 13: %s
Library ID: %s
'''%(self.title, self.author, self.publisher, self.isbn_10, self.isbn_13, self.library_id)
        return s

    def __eq__(self, other):
        if self.library_id == other.library_id:
            return True
        else:
            return False

class CatalogEntry(Record):
    def __init__(self, isbn, copies = 1, title='', author=''):
        Record.__init__(self, '', isbn, title, author)
        self.copies = copies
        
    def __repr__(self): #Method of displaying/printing/stringifying an object.
        s = '''
Title: %s
Author: %s
Publisher: %s
ISBN: %s
Copies: %i
''' %(self.title, self.author, self.publisher, self.isbn, self.copies)
        return s

    def __eq__(self, other): #The thing that says if two catalog entries are the same
        if self.title != other.title:
            return False
        elif self.author != other.author:
            return False
        elif self.isbn_10 != '' and other.isbn_10 != '' and self.isbn_10 != other.isbn_10:
            return False
        elif self.isbn_13 != '' and other.isbn_13 != '' and self.isbn_13 != other.isbn_13:
            return False
        else:
            return True

