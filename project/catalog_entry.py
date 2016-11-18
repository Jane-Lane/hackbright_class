def strip_isbn(isbn): #takes out non-numeric characters
    digits = [x for x in isbn if x in '0123456789']
    isbn = ''.join(digits)
    return isbn

class CatalogEntry(object):
    def __init__(self, isbn, title='', author=''):
        isbn = strip_isbn(isbn)
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
        self.all_publishers = []
        self.lccn = ''
        self.isbn_13 = self.isbn
        self.copies = 1
        
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

