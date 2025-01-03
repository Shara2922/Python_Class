# Python_Class
## Introduction to Python



## Python Syntax

Python uses indentation to define blocks of code.
Code is executed line by line.

### Example: Hello World

```python
print("Hello World!")
```

## Python Variables

Variables store data and are created when you assign a value.
Creating Variables

    Use = to assign a value to a variable.
    No need to declare the type; Python infers it automatically.

### Example:

x = 5          # Integer
y = 3.14       # Float
name = "Alice" # String

## Naming Rules

    Must start with a letter or underscore _.
    Cannot start with a number.
    Can contain letters, numbers, and underscores.
    Case-sensitive (name and Name are different).

## Printing Variables

Use the print() function to display variables:

print(x)
print("Hello, " + name)  # String concatenation

## Variable Types

    Integer (int): Whole numbers.
    Float (float): Decimal numbers.
    String (str): Text data.
    Boolean (bool): True or False.

### Example:

is_student = True
pi = 3.14
age = 25
name = "John"

Reassigning Variables

Variables can be updated:

x = 10
x = x + 5  # x now equals 15

Multiple Assignments

You can assign multiple variables in one line:

a, b, c = 1, 2, "Hello"

## Basic Input and Output

    Get user input using the input() function.

    name = input("What is your name? ")
    print("Hello, " + name)

## Python is Dynamic

    Python allows you to change the type of a variable:

x = 5       # x is an integer
x = "five"  # x is now a string