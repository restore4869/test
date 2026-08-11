# Object-Oriented Programming — Finish the Code
# Instructions:
# Complete the missing line(s) of code for each question.
# Do NOT remove existing code.


# --------------------
# Question 1
# --------------------
class App:
    def __init__(self, name):
        self.name = name


# TODO: Create an App object with the name "Google Maps"
app = App("Google Maps")

print()
# --------------------
# Question 2
# --------------------
class Car:
    def __init__(self, brand):
        self.brand = brand


my_car = Car("Toyota")

# TODO: Print the brand of my_car
print(my_car.brand)

print()
# --------------------
# Question 3
# --------------------
class Person:
    def greet(self):
        print("Hello!")


p = Person()

# TODO: Call the greet method
p.greet()

print()
# --------------------
# Question 4
# --------------------
class Student:
    name = "David"
    def __init__(self, name):
        # TODO: Store name as an instance variable
        self.name = name    #pass  #HW 1/13/26: look up what instance variable is for python.        
#Google: instance variable: a variable that is unique to a specific object(instance) of a class.

print()
'''Google: class Dog:
    def __init__(self, name, breed):
    #storing variables using self.
        self.name = name
        self.breed = breed
    #creating instances using unique data.
my_dog = Dog("husk", "Golden retriever")
your_dog = Dog("hound", "Beagle")
print(my_dog.name)
print(your_dog.breed)'''
# --------------------
# Question 5
# --------------------
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance


# TODO: Create an account with the default balance
account = BankAccount()
print(account.balance)

print()
# --------------------
# Question 6
# --------------------
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        # TODO: Increase count by 1
        self.count += 1 #pass 
#self refers to the current instance of a class.

print()
# --------------------
# Question 7
# --------------------
class Animal:
    def speak(self):
        print("Some sound")


# TODO: Make Dog inherit from Animal
class Dog(Animal):
    pass

print()

# --------------------
# Question 8
# --------------------
class Animal:
    def speak(self):
        print("Some sound")


class Cat(Animal):
    # TODO: Override speak to print "Meow"
    def speak(self):
        print("Meow")

claw = Cat()
claw.speak()

print()
# --------------------
# Question 9
# --------------------
class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    def __init__(self, name, department):
        # TODO: Call the parent constructor
        super().__init__(name)
        self.department = department

employee = Employee("employee of the month")
manager = Manager("employer", "supervisor")
print(manager.department)
print(manager.name)
print(employee.name)

print()
# --------------------
# Question 10
# --------------------
class User:
    def __init__(self, password):
        # TODO: Make password a private attribute
        #pass
        self._password = password
        #HW questions 10 and 18  01/27/26.
        #hint: has to be an instance variable.
code = User('password')
print(code._password)

print()

# --------------------
# Question 11
# --------------------
class Player:
    total_players = 0

    def __init__(self, name):
        self.name = name
        # TODO: Increment total_players when a Player is created
        #pass
        Player.total_players += 1

print()

# --------------------
# Question 12
# --------------------
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        # TODO: Return a string like "Book: <title>"
        #pass
        #print(f"Book: {self:title}")
        #print(f"Book: {self.title}")
        return f"Book: {self.title}"
#HW 03/01/26: review this question 12 about the __str__.

print()

# --------------------
# Question 13
# --------------------
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [Shape(), Square(4)]

# TODO: Print the area of each shape
for shape in shapes:
    #pass
    #print(Shape.shapes())
    #print(Shape.self())
    #print(shapes.area())
    #print(Shape.area())
    print(shape.area())


print()

#HW: solve questions 11, 12, and 13.
#HW: Find what the concept inside question 13 either abstraction, encapsulation, inheritance, and polymorphism.
#Hint: it's in the area method.
#The concept inside this question is polymorphism. 

#super(): A function used to call methods from a parent class.
'''Decorator: A specific language feature and a design pattern using the @ syntax to extend functionality,
    takes another function, and returns a new upgraded version without changing the original function.'''


#HW: solve questions 14, 15, and 19.
# --------------------
# Question 14
# --------------------

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        # TODO: Start the engine
        #pass
        #Engine.start()
        self.engine.start()

toyota = Car()
toyota.start_car()

print()

# --------------------
# Question 15
# --------------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #@property
    def area(self):
        # TODO: Return the area
        
        #Google: Return the area by multiplying width and height
        return self.width * self.height

box = Rectangle(5, 10)
print(box.area())

print()

# --------------------
# Question 16
# --------------------
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        # TODO: Call parent send, then print "Email sent"
        super().send()
        print("Email sent")
gmail = EmailNotification()
gmail.send()

print()

# --------------------
# Question 17
# --------------------
class Animal:
    pass


class Dog(Animal):
    pass


a = Dog()

# TODO: Check if a is an Animal and print "Yes" if true
pass

print()

# --------------------
# Question 18
# --------------------
class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        # TODO: Return the balance
        #pass
        return self._balance
equal = Account("3,000,000")
print(equal.get_balance())

print()

# --------------------
# Question 19
# --------------------
class Calculator:
    def add(self, a, b):
        return a + b

    def double_sum(self, a, b):
        # TODO: Return double the sum using add()
        #pass
        #return double_sum * 2
        #self.add.a.b()
        sum = self.add(a, b)
        return sum * 2
    
calc = Calculator()
print(calc.add(5, 10))
print(calc.double_sum(5, 10))

print()

# --------------------
# Question 20
# --------------------
class Employee:
    def calculate_pay(self):
        # TODO: Force subclasses to implement this method
        pass
