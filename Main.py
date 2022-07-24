from Store2 import Store 

def main():
 
    
    choice = 0
    # Selection 
    while choice !=4:
        print("\n*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1* WELCOME to my BookStore... *1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*\n")
        print("1) Add a book")
        print("2) Search the book")
        print("3) Display books")
        #print("4) Buy books")
        print("4) Quit")
        choice = int(input())
        
        # Adding a book
        if choice == 1:
            Store.AddaBook()
        
        # Searching for a book        
        elif choice == 2:
            Store.SearchBook()

            # Displaying all books
        elif choice == 3:
            Store.DisplayBook()
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
            Store.quit()
    #os.system('cls')
    # Saving to external CSV file

   
if __name__ == "__main__":
    main()