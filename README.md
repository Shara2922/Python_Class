# Python_Class
## Introduction to Python
Python is a popular, high-level programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, automation, and many other fields.

## Key Features of Python:
 ● Easy to Learn: Python has a clean and straightforward syntax, making it beginner friendly.
 
 ●  Interpreted Language: Code is executed line by line, which makes debugging easier.
 
 ●  Dynamically Typed: You don’t need to declare the type of a variable.
 
 ● Versatile: Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
 
 ● Extensive Libraries: It has a vast standard library and many third-party libraries for specialized tasks.

## Python Syntax

Python uses indentation to define blocks of code. Code is executed line by line.

### Example: Hello World

``print("Hello, World!")
``

## Python Variables

Variables store data and are created when you assign a value.
Creating Variables

## Printing Variables

Use the print() function to display variables:

`print(x)
print("Hello, " + name)  # String concatenation
`
## Variable Types

● Integer (int):  Integers are whole numbers.

  `my_number = 354
  `

● Float (float):  Floats are numbers with decimal places.When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always bea floating point number.

`pi = 3.14
`

● String (str):  A string is just a string of characters. It should be surrounded by double quotes.

 `name = "Shara"
 `
 
● Boolean (bool): True or False.

`is_student = True
`

## Input-Output Function
The input() function in Python is used to take user input from the console. It always returns the input as a string, so you may need to convert it to other data types if required.
Basic Syntax:

    variable = input(prompt)

prompt: A string that is displayed to the user to explain what kind of input is expected.

Examples:
1. Simple Input
   
```name = input("Enter your name: ")
     print(f"Hello, {name}!")

Output: Enter your name: Alice
     Hello, Alice!
```

2. Numeric Input

Since input() always returns a string, you need to convert it to an integer or float using int() or float():

```age = int(input("Enter your age: "))
print(f"You are {age} years old.")

Output: Enter your age: 25
You are 25 years old.
```

3. Multiple Inputs (Using Split)
You can use the split() method to take multiple inputs at once:

```x, y = input("Enter two numbers separated by space: ").split()
print(f"x: {x}, y: {y}")

Output:
Enter two numbers separated by space: 10 20
x: 10, y: 20
```
