#from Main import main
import logging
import re
import os
booksList = []
cartList = []
class Store:   

    def __init__(self, nBook, nAuthor, nType, nPages, nPrice):
        self.a1 = nBook
        self.a1 = nAuthor
        self.a1 = nType
        self.a1 = nPages
        self.a1 = nPrice
              

    def append_list_as_row(file_name, booksList):
    
        try:    
        
            infile = open("theBooksList.csv", "r")
            line = infile.readline()
            while line:
                booksList.append(line.rstrip("\n").split(",") )
                line = infile.readline()
            infile.close()
        # Exception   
        except FileNotFoundError :
            print("the <bookslist.csv> file is not found ")
            print("Starting a new books list!")
            booksList = [] 

    def append_list_as_row1(file_name, cartList):
    
        try:    
        
            infile1 = open("theCartList.csv", "r")
            line = infile1.readline()
            while line:
                cartList.append(line.rstrip("\n").split(",") )
                line = infile1.readline()
            infile1.close()
        # Exception   
        except FileNotFoundError :
            print("the <CartList.csv> file is not found ")
            print("Starting a new Cart list!")
            cartList = []  


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
                nAuthor = input("Enter the name of the author \n>>>")
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
                nType = input("Type of the Book\n>>>")
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
                nPages = str(input("Enter the number of pages \n>>>"))
            except ValueError as ve:
                print("\nCANNOT ENTER A STRING FOR AGE! PLEASE ENTER AN INTEGER!\n")
                logging.error("Tried to enter a string for page, trying again...")
            else:
                break
        while True:
            try:
                nPrice = str(input("Price of the book? \n>>>"))
            except ValueError as ve:
                print("\nCANNOT ENTER A STRING FOR AGE! PLEASE ENTER AN INTEGER!\n")
                logging.error("Tried to enter a string for page, trying again...")
            else:
                break
        (booksList.append([nBook, nAuthor, nType, nPages, nPrice]))
    
    def SearchBook():
        print("Search here the book you want...")
        keyword = input("Enter Search Term: ")
        for book in booksList:
            if keyword in book:
                print(book)

    def AddtoCart():
        ChooseBook = input("Which book do you like to add to cart? >>>")
        for item in booksList:
            if ChooseBook in item:
                print("The", item, "is added to your cart")
                booksList.remove(item)
                cartList.append(item)
    
    
    def DisplayBook():
        print("*******Here are my books...*******")
        #for i in range(len(booksList)):
        print(*booksList, sep ="\n")

    def ViewCart():
        print("Items in cart")
        print(*cartList, sep="\n")

    def BuyBook():
        key = input("Search here...")
        for buybook in booksList:
            if key in buybook:
                print("Thank you for purchasing the",buybook, "We will send it your address")
                booksList.remove(buybook)
                booksList.append
        if key not in buybook:
            print("SORRY!! The book you are looking for is out of order...")

    def quit():
        print("BYE BYE!!")

        outfile = open("theBooksList.csv", "w")
        for book in booksList:
            outfile.write(",".join(book) + "\n")
        outfile.close()

        outfile1 = open("theCartList.csv", "w")
        for books in cartList:
            outfile1.write(",".join(books) + "\n")
        outfile1.close()
    append_list_as_row('theBooksList.csv', booksList)
    append_list_as_row1('theCartList.csv', cartList)