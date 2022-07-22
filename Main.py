from Store import Books, SearchBook, AddBook, DisplayBook
import logging
import re
import os
def main():
   
 
    try:    
        
        booksList = []

        # initialize books list
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
    
    choice = 0

    # Selection 
    while choice !=4:
        print("\n*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1* WELCOME to my BookStore... *1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*\n")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        #print("4) Buy books")
        print("4) Quit")
        choice = int(input())
        
        # Adding a book
        if choice == 1:
            print("Addig a book...")
            while True:
                try:
                    nBook = int(input("\nEnter the name of the book:\n>>>"))
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
            
                
        # Searching for a book        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)
            else:
                print("*********************************************\n\nSORRY!! The book you are looking for is out of stock\n\n*********************************************")
        # Displaying all books
        elif choice == 3:
            print("*******Here are my books...*******")
            for i in range(len(booksList)):
                print(booksList[i])
        # elif choice == 4:
        #     print("Please choose the book you want to buy")
        #     Buy = input("Name of the book you are looking for")
        #     for buyBooks in booksList:
        #         if Buy in buyBooks:
        #             print("We have shipped the book to your Address")
        #             booksList.pop.buyBooks[i]
        #         else:
        #             ("Sorry!! The book you are searching for is out of order")
                    

        elif choice == 4:
            print("BYE BYE!!")
    print("Thats all the options we have in our Store")
    #os.system('cls')
    # Saving to external CSV file
    outfile = open("theBooksList.csv", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()
if __name__ == "__main__":
    main()