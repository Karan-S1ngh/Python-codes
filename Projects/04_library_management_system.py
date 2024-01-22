# Library Management System

class Library :
    
    def __init__(self, listOfBooks) :
        self.books = listOfBooks
        
    def displayAvailableBooks(self) :
        print("Books present in this library are: ")
        for book in self.books :
            print(" *" + book)
            
    def borrowBook(self, bookName) :
        if bookName in self.books :
            print(f"You have been issued '{bookName}'. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else :
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
        
    def returnBook(self, bookName) :
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
                        
            
class Student :
        
        def requestBook(self) :
            self.book = input("Enter the name of the book you want to borrow: ")
            return self.book
        
        def returnBook(self) :
            self.book = input("Enter the name of the book you want to return: ")
            return self.book

if __name__ == "__main__" :
    centralLibrary = Library(["Python", "Django", "Flask", "Pandas", "Algorithms"])    
    # created object for Library class
    centralLibrary.displayAvailableBooks()
    student = Student()             
    # created object for Student class
    while(True):
        welcomeMsg = '''
        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1 :
            centralLibrary.displayAvailableBooks()
        elif a == 2 :
            centralLibrary.borrowBook(student.requestBook())  # Modified line
        elif a == 3 :
            centralLibrary.returnBook(student.returnBook())  # Modified line
        elif a == 4 :
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else :
            print("Invalid Choice!")
          
          
          
  
# in the above system
# all available books are displayed
# the student can borrow a book, add a new book and return a book

# this is a basic library management system
# can be made for multiple students and libraries
# can be made more interactive, secure and user friendly
# can be made more efficient and robust




'''OUTPUT
Books present in this library are: 
 *Python
 *Django
 *Flask
 *Pandas
 *Algorithms

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 2
Enter the name of the book you want to borrow: Python
You have been issued 'Python'. Please keep it safe and return it within 30 days

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 1
Books present in this library are:
 *Django
 *Flask
 *Pandas
 *Algorithms

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 3
Enter the name of the book you want to return: Web development
Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 1
Books present in this library are:
 *Django
 *Flask
 *Pandas
 *Algorithms
 *Web development
 
        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 0
Invalid Choice!

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 2
Enter the name of the book you want to borrow: Java
Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available

        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

Enter a choice: 4
Thanks for choosing Central Library. Have a great day ahead!
'''
