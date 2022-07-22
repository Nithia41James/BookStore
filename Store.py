from abc import ABC, abstractmethod


booksList = []

class Books(ABC):
    def __init__(self, nBook, nAuthor, nType, nPages):
        self._nBook = str(nBook)
        self._nAuthor = str(nAuthor)
        self._nType = str(nType)
        self._nPages = int(nPages)

    def setName(self, nBook):
        self._nBook = str(nBook)

    def getName(self):
        return self._nBook

    @abstractmethod
    def reed(self):
        pass

    def turnPages(self, years=1):
        pass
    

    def __str__(self):
        return "Nameof the book: " + self._nBook + ", Name of the Author: " + self._nAuthor + ", Read it before?: " + self._nType + ", Number of pages: " + self._nPages

class AddBook(Books):
    def BookAddedd(self):
        pass

class SearchBook(Books):
    def BookSearched(self):
        pass
    
class DisplayBook(Books):
   pass

