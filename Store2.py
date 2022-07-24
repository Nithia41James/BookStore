#from Main import main
import logging
import re
import os
booksList = []
class Store:
    #booksList = []
    
    try:    
     
        infile = open("theBooksList.csv", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(",") )
            line = infile.readline()
        infile.close()
     # Exception   
    except FileNotFoundError :
        print("the <bookslist.txt> file is not found ")
        print("Starting a new books list!")
        booksList = []   

    def AddaBook():
        print("Addig a book...")
        while True:
            try:
                nBook = input("\nEnter the name of the book:\n>>>")
                check = re.search(',', nBook)

                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("\nCANNOT HAVE COMMAS IN BOOK NAME!\n")
                logging.error("Tried to enter a comma for name of the book, trying again...")
            else:
                break
        
        while True:
            try:
                nAuthor = input("Enter the name of the author >>>")
                check = re.search(',', nAuthor)

                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("\nCANNOT HAVE COMMAS IN NAME!\n")
                logging.error("Tried to enter a comma for name, trying again...")
            else:
                break
        
        while True:
            try:
                nType = input("Type of the Book> >>>")
                check = re.search(',', nType)

                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("\nCANNOT HAVE COMMAS IN type of the Book!\n")
                logging.error("Tried to enter a comma for Book type, trying again...")
            else:
                break
        
        while True:
            try:
                nPages = str(input("Enter the number of pages >>>"))
            except ValueError as ve:
                print("\nCANNOT ENTER A STRING FOR AGE! PLEASE ENTER AN INTEGER!\n")
                logging.error("Tried to enter a string for page, trying again...")
            else:
                break
        (booksList.append([nBook, nAuthor, nType, nPages]))
    
    def SearchBook():
        #booksList = []
        print("Search here the book you want...")
        keyword = input("Enter Search Term: ")
        for book in booksList:
            if keyword in book:
                print(book)

    def DisplayBook():
        #booksList = []
        print("*******Here are my books...*******")
        for i in range(len(booksList)):
            print(booksList[i])

    outfile = open("theBooksList.csv", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()