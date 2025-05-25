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
    # 5. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
    # Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# 6. Write a function called check-season, it takes a month parameter and
# returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month. Please enter a number between 1 and 12."
# 7. Declare a function called calculate_slope which returns the slope of a linear function.
def calculate_slope(y2, y1, x2, x1):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    return (y2 - y1) / (x2 - x1)