# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
# 2. Declare a function add_three_numbers. It takes three parameters and it returns a sum.
def add_three_numbers(a, b, c):
    return a + b + c
# 3. Area of a circle is calculated as follows: area = π x r x r.
# Write a function that calculates area_of_circle.
import math
def area_of_circle(radius):
    return math.pi * radius * radius
# 4. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All arguments must be numbers."