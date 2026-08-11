# object oriented programming (OOP)
# object oriented design (OOD)

# an object is a specific instance of a class
# a class is a blueprint for an object

# terminology
#     - method = function
#     - field = attribute = feature

# 4 OOP pillars: abstraction, encapsulation, inheritance, polymorphism

# Abstraction (simply the zoo for outsiders):
#     - hiding complex logic and exposing only what’s necessary

# Encapsulation (keep the zoo organized):
#     - grouping related data and methods inside separate classes
#     - hiding internal details so you interact with an object through its public interface

# Inheritance (reuse animals):
#     - lets you create new classes based on existing ones,
#       so you don’t have to rewrite common logic.

# Polymorphism (different animals, same action):
#     - different classes having the same method name but implement it differently

# UML (unified modeling language) diagram

from abc import ABC, abstractmethod


# abstract class (Animal)
class Animal(ABC):  # abstraction
    def __init__(self, name):  # constructor method
        self.name = name
#Cannot instantiate abstract classes.
    @abstractmethod
    def speak(self):
        print("An animal makes a noise")

    def sleep(self):
        print(self.name + " is sleeping.")


# dog class
class Dog(Animal):  # inheritance
    def speak(self):  # polymorphism
        print(self.name + " says: Woof!")

    def fetch(self, item):
        print(self.name + " fetches the " + item + ".")

    def wag_tail(self):
        print(self.name + " is wagging its tail happily!")


# cat class
class Cat(Animal):  # inheritance
    def speak(self):  # polymorphism
        print(self.name + " says: Meow!")

    def climb(self):
        print(self.name + " climbs onto the windowsill.")

    def purr(self):
        print(self.name + " is purring softly.")


print()  # print an empty line

buddy = Dog("Buddy")  # instantiation = making a new object using a class
whiskers = Cat("Whiskers")

animals = [buddy, whiskers]

for animal in animals:
    animal.speak()
    animal.sleep()

print()  # print an empty line

buddy.fetch("ball")
buddy.wag_tail()

print()  # print an empty line

whiskers.climb()
whiskers.purr()

print()  # print an empty line
