"""
Python 3.4+
Gianluca Truda - gianlucatruda@gmail.com
SimplePay Coding Exercise
October 2016
---------------------------
A robot on a grid has starting position (0,0).
The robot can be given instructions to move a given number of steps up, down, left, or right.
Write a function that takes in a list of instructions and outputs the distance (in a straight line) the
robot is from its starting position. The distance should be rounded to the nearest integer.
The instructions are given as a single array of directions followed by a number of steps
to be taken in that direction.

NOTE: I assumed the grid was a Cartesian plane.
"""
import math


def my_round(x):
    """
    A simple rounding function to overcome Python's inherent rounding down.
    Instead it rounds up 0.50 and greater, whilst rounding down 0.49 and lower.
    :param x: a floating point value.
    :return: a rounded integer value.
    """
    rem = 10*float(x - int(x))
    if rem >= 5:
        return int(x)+1
    else:
        return int(x)

# User input is take in.
in_values = input("\nPlease enter a set of instructions of the form \n"
                  "UP 5, DOWN 3, LEFT 3, RIGHT 2, UP 2, LEFT 1\n\n")

# The input is split into individual strings and fed into the array.
instructions = []
for s in in_values.split(", "):
    instructions.append(s)

# Variables for the change in each plane are instantiated.
x_delta = 0
y_delta = 0

# Every instruction from the given input is processed and the if-statements filter the changes to the
# appropriate delta value with the appropriate sign.
for e in instructions:
    if "UP" in e:
        x_delta += int(e[e.find(" ")+1:])
    elif "DOWN" in e:
        x_delta -= int(e[e.find(" ")+1:])
    elif "LEFT" in e:
        y_delta += int(e[e.find(" ")+1:])
    elif "RIGHT" in e:
        y_delta -= int(e[e.find(" ")+1:])

# The resulting delta values in both planes are processed with the Pythagorean equation
# and rounded using my custom rounding function.
out_val = my_round((math.sqrt(math.pow(x_delta, 2) + math.pow(y_delta, 2))))

# Output to command line.
print(out_val)

