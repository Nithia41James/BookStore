from Store2 import Store 

def main():
 
    
    choice = 0
    # Selection 
    while choice !=5:
        print("\n*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1* WELCOME to my BookStore... *1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*\n")
        print("1) Add a book")
        print("2) Search the book")
        print("3) Display books")
        print("4) Buy books")
        print("5) Quit")
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

        # Purchasing a boook
        elif choice == 4:
            Store.BuyBook()
        #Quit the program            
        elif choice == 5:
            Store.quit()
    #os.system('cls')
    # Saving to external CSV file

   
if __name__ == "__main__":
    main()