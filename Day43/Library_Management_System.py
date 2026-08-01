# Day43 - Mini Project
# Library Management System



class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def show_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print("Title               :", self.title)
        print("Author              :", self.author)
        print("Availability Status :", status)
        print("-" * 20)


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # FIXED: Added borrowed_books list

    def calculate_late_fee(self, days_late):
        return days_late * 10


class Student(Member):

    def __init__(self, name, member_id, grade):
        super().__init__(name, member_id)
        self.grade = grade

    def calculate_late_fee(self, days_late):
        fee = days_late * 10
        return fee  # FIXED: Return fee directly (integer)


class Teacher(Member):

    def __init__(self, name, member_id, department):
        super().__init__(name, member_id)
        self.department = department

    def calculate_late_fee(self, days_late):
        fee = days_late * 5
        return fee  # FIXED: Return fee directly (integer)


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book_obj):
        self.books.append(book_obj)
        print(book_obj.title, ": Book Added")

    def show_available_books(self):
        print("\n--- Available books ---")
        found = False
        for b in self.books:
            if b.is_available:
                b.show_info()  # FIXED: Corrected dot syntax
                found = True
        if not found:
            print("No books Currently Available")

    def borrow_book(self, title, member):  # FIXED: Renamed to borrow_book
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_available:
                    b.is_available = False
                    member.borrowed_books.append(b)
                    print(f"Success: {member.name} borrowed '{b.title}'.")
                    return
                else:
                    print(f"Sorry, '{b.title}' is already borrowed.")
                    return
        print(f"Error: Book '{title}' not found in catalog.")

    def return_book(self, title, member, days_late=0):
        for b in self.books:
            if b.title.lower() == title.lower() and b in member.borrowed_books:
                b.is_available = True
                member.borrowed_books.remove(b)
                fee = member.calculate_late_fee(days_late)
                print(f"Success: '{b.title}' returned by {member.name}.")
                if days_late > 0:
                    print(f"Late Fee Due ({days_late} days late): Rs. {fee}")
                return
        print(f"Error: {member.name} does not have '{title}' checked out.")



city_library = Library()

# Add Books
city_library.add_book(Book("Python Basics", "Guido van Rossum"))
city_library.add_book(Book("Clean Code", "Robert Martin"))
city_library.add_book(Book("Design Patterns", "Erich Gamma"))

# Create Members
student1 = Student("Het", "S101", "12th Grade")
teacher1 = Teacher("Dr. Pankaj", "T501", "Computer Science")



city_library.show_available_books()

# Borrowing
print("\n--- Borrowing Books ---")
city_library.borrow_book("Clean Code", student1)
city_library.borrow_book("Design Patterns", teacher1)

# Check Catalog
city_library.show_available_books()

# Returning
print("\n--- Returning Books ---")
city_library.return_book("Clean Code", student1, days_late=3)
city_library.return_book("Design Patterns", teacher1, days_late=5)