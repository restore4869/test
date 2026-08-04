# TODO: Q1
# Create an enum called Direction with four members: NORTH, SOUTH, EAST,
# and WEST, assigned values 1 through 4. Print the name and value of WEST.

from enum import Enum

class Direction(Enum):

    NORTH = "1"
    SOUTH = "2"
    EAST = "3"
    WEST = "4"

print(Direction.WEST.name)
print(Direction.WEST.value)

print()

# TODO: Q2
# Given a Planet enum with members MERCURY = 1, VENUS = 2, EARTH = 3, and MARS = 4,
# write code that accesses the EARTH member both by its name
# (using bracket notation) and by its value (using the callable syntax). Print both results.

class Planet(Enum):
    MERCURY = "1"
    VENUS = "2"
    EARTH = "3"
    MARS = "4"

by_name = Planet["EARTH"]
by_value = Planet("3")
print(by_name)
print(by_value)

print()

# TODO: Q3
# Create a Month enum containing JANUARY through DECEMBER (values 1–12).
# Write a loop that prints each month's value and name in this format:
# 1 - January
# 2 - February
# ...
# Hint: use .name.capitalize())

class Month(Enum):

    JANUARY = '1'
    FEBRUARY = '2'
    MARCH = '3'
    APRIL = '4'
    MAY = '5'
    JUNE = '6'
    JULY = '7'
    AUGUST = '8'
    SEPTEMBER = '9'
    OCTOBER = '10'
    NOVEMBER = '11'
    DECEMBER = '12'

for months in Month:
    #print(months.value)
    #print(months.name.capitalize())
    #print(months.value, "-", months.name.capitalize())
    print(f"{months.value} - {months.name.capitalize()}")
print()

# TODO: Q4
# Create a TrafficLight enum with members RED, YELLOW, and GREEN.
# Build a dictionary that maps each member to an action string (e.g., "Stop", "Caution", "Go").
# Then write a function get_action(light) that accepts a TrafficLight member and returns the correct action.

class TrafficLight(Enum):

    RED = "Stop"
    YELLOW = "Caution"
    GREEN = "Go"

#Google: Dictionary mapping Enum members to action strings

actions = {
    TrafficLight.RED: "Stop",
    TrafficLight.YELLOW: "Caution",
    TrafficLight.GREEN: "Go"
    }
def get_action(light: TrafficLight):
    return actions[light]
    #return light
print(f"result: {get_action(TrafficLight.GREEN)}")
print(get_action(TrafficLight.RED))
print(get_action(TrafficLight.YELLOW))