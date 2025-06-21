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
# 8. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Coefficient 'a' cannot be zero."
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions."
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"One solution: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two solutions: x1 = {x1}, x2 = {x2}"
    # 9. Declare a function called print_list which takes a list as a parameter and prints each item in the list.
def print_list(items):
    if isinstance(items, list):
        for item in items:
            print(item)
    else:
        return "Input must be a list."
# 9. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    
    # Check for factors from 3 to sqrt(n), skipping even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True