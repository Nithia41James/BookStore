from Store2 import Store 

def main():
 
    
    choice = 0
    # Selection 
    while choice != 6:
        print("\n*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1* WELCOME to my BookStore... *1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*\n")
        print("1) Add a book")
        print("2) Search the book")
        print("3) Display books")
        print("4) Add books to cart")
        print("5) Buy books")
        print("6) Quit")
        choice = int(input(">>>"))
        
        # Adding a book
        if choice == 1:
            Store.AddaBook()
        
        # Searching for a book        
        elif choice == 2:
            Store.SearchBook()

        # Displaying all books
        elif choice == 3:
            Store.DisplayBook()

        elif choice == 4:
            Store.AddtoCart()

        # Purchasing a boook
        elif choice == 5:
            Store.BuyBook()
        #Quit the program            
        elif choice == 6:
            Store.quit()

   
if __name__ == "__main__":
    main()