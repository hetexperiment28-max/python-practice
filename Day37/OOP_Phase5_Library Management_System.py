# Day37 Phase5
# Relationship between objects
# Topic : Library Management_System

class book:

    def __init__(self, Title, Author):
        self.title = Title
        self.author = Author
        self.available = True

    def show_info(self):
        print("title :", self.title)
        print("Author :", self.author)
        print("Available :", self.available)
        print("-" * 10)

    def borrow(self):
        if self.available :
            self.available = False
            print("Book has been Borrowed") 

        else:
            print("Already Borrowed")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "is Return Successfull")

        else:
            print(self.title, "is Already in library")


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book_obj):
        if book_obj not in self.books: 
            self.books.append(book_obj)
            print("Book Added to the library")
        else:
            print("Book is already Listed")

    def show_books(self):
        print("-----Library Collection-----", "\n")
        for b in self.books:
            b.show_info()

    def search(self, title):
        for b in self.books:
            if title.lower() in self.books.lower():
                
                if b.available :
                    return("Available")
            
        else:
            return("Not Available in catalog")

    def borrow_book(self,title):
        for b in self.books:
            if title.lower() == b.title.lower():
                b.borrow()
                return
        print("Book title not found in library")

    def return_book(self, title):
        for b in self.books:
            if title.lower() == b.title.lower():
                b.return_book()
                return
        print("Book title not found in library")

library = Library()

library.add_book(book("Hello","Het"))
library.add_book(book("Healing","elive"))
library.add_book(book("Magic of maths","Pankaj"))
library.add_book(book("What is science","Raj"))
library.add_book(book("Stars vs me","Lucky"))


while True:

    print(" 1. Show Books", "\n", "2. Search Book", "\n", "3. Borrow Book", "\n",
          "4. Return Book", "\n", "5. Exit", "\n")

    try:
        in_choice = False
        choice = int(input("Enter menu choice (1-5):"))
        if 1<= choice <= 5:
            in_choice = True
        if not in_choice:
            print("choice not in menu")
            continue
    except ValueError:
        print("Enter valid input in integer range (1-5).")
        continue


    match choice:

        case 1:
            library.show_books()

        case 2: 
            title = input("Enter book title to search from Library")
            print(library.search(title))

        case 3:
            title = input("Enter book title to borrow: ")
            library.borrow_book(title) 
            print("-" * 20)

        case 4:
            title = input("Enter book title to return: ")
            library.return_book(title)  
            print("-" * 20)

        case 5:
            print("Program Exiting...")
            break
