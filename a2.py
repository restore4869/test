#These are modules. 
from abc import ABC
from datetime import date
from enum import Enum

# ------------------------
# Custom Enums
# ------------------------

class Genre(Enum):

    FICTION = 'fiction genre'
    NONFICTION = 'nonFiction genre'
    SCIENCE = 'Science genre'
    HISTORY = 'History genre'
    TECHNOLOGY = 'Technology genre'

class Member_type(Enum):

    STUDENT = 'student members'
    FACULTY = 'faculty members'
    GUEST = 'guest members'

class Status(Enum):

    AVAILABLE = 'available status'
    BORROWED = 'borrowed status'
    OVERDUE = 'overdue status'


# ------------------------
# Helper classes
# ------------------------

class Name:
    def __init__(self, first: str, last: str):
# Initialize Name attributes
        self.first = first
        self.last = last

    def __str__(self):
# Return a readable string representation
        return f"{self.first} {self.last}"


class Book:
    def __init__(self,
        title: str,
        author: Name,
        genre: Genre,
        status: Status,
        borrow_date: date,
        due_date: date):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.borrow_date = borrow_date
        self.due_date = due_date


#--------------------
# Abstract class
#--------------------

class Member(ABC):
    def __init__(self,
                name: Name,
                member_type: Member_type):
        self.name = name
        self.member_type = member_type
        self.borrow_books = []

#--------------------
# Child classes
#--------------------


class Student(Member):
    def __init__(self, name, student_id:str, major:str, max_books: int):
        super().__init__(name, Member_type.STUDENT)
        self.student_id = student_id
        self.major = major
        self.max_books = 3  # Students get a limit of 3
        

class Faculty(Member):
    def __init__(self, name, faculty_id: str, department: str, max_books: int):
        super().__init__(name, Member_type.FACULTY)
        self.faculty_id = faculty_id
        self.department = department
        self.max_books = 5 # Faculty get a limit of 5

class Guest(Member):
    def __init__(self, name, email:str, expiry_date: date):
        super().__init__(name, Member_type.GUEST)
        self.email = email
        self.expiry_date = expiry_date
        

#--------------------
# Library Class
#--------------------

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def show_books(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)


