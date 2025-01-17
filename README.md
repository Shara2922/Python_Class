# Python_Class
## Introduction to Python
Python is a popular, high-level programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, automation, and many other fields.

## Content
- [Key Features of Python](#key_features_of_python)
- [Python Syntax](#python_syntax)
- [Errors](#errors)
- [Printing Variables and Variable Types](#printing_variables_and_variable_types)
- [Input-Output Function](#input_outpurt_function)
- [Operators](#operators)
- [Strings](#strings)
- [Python Homework](https://github.com/Shara2922/Python_Class/blob/main/Python_homework.py)
## Key Features of Python:
 ● Easy to Learn: Python has a clean and straightforward syntax, making it beginner friendly.
 
 ●  Interpreted Language: Code is executed line by line, which makes debugging easier.
 
 ●  Dynamically Typed: You don’t need to declare the type of a variable.
 
 ● Versatile: Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
 
 ● Extensive Libraries: It has a vast standard library and many third-party libraries for specialized tasks.

## Python Syntax

 Python uses indentation to define blocks of code. Code is executed line by line.

      print("Hello, World!")

## Errors

Syntax Error:
 Syntax errors happen when your code does not make any sense to the computer. This can happen because you've misspelt something or there's too many brackets or a missing comma.

      print(12 +4))
      File "<stdin>", line 1
      print(12 + 4))
      ^
      SyntaxError: unmatched ')'

Indentation Error:
 Indentation error occurs when the number of space at the begining of a block is not equal to the number of space assigned at the end. This is root caused of the Indentation error.

      f height >= 120
      rint("You can ride the rollercoaster")
      lse:
      rint("Sorry you have to grow taller to ride the rollercoaster")

      Output: Indentation error.

## Printing Variables and Variable Types

 Use the print() function to display variables:

      print(x)
      print("Hello, " + name)  # String concatenation
 
Integer (int):  Integers are whole numbers.

      my_number = 354
  
Float (float):  Floats are numbers with decimal places.When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always bea floating point number.

      pi = 3.14

String (str):  A string is just a string of characters. It should be surrounded by double quotes.

      name = "Shara"
 
 
Boolean (bool): True or False.

      is_student = True


## Input-Output Function
The input() function in Python is used to take user input from the console. It always returns the input as a string, so you may need to convert it to other data types if required.
Basic Syntax:

      variable = input(prompt)

      prompt: A string that is displayed to the user to explain what kind of input is expected.

Simple Input
   
      name = input("Enter your name: ")
      print(f"Hello, {name}!")

      Output: Enter your name: Shara
      Hello, Shara!

Numeric Input

 Since input() always returns a string, you need to convert it to an integer or float using int() or float ():

      age = int(input("Enter your age: "))
      print(f"You are {age} years old.")

      Output: Enter your age: 25
      You are 25 years old.


Multiple Inputs (Using Split)

 You can use the split() method to take multiple inputs at once:

      x, y = input("Enter two numbers separated by space: ").split()
      print(f"x: {x}, y: {y}")

      Output:
      Enter two numbers separated by space: 10 20
      x: 10, y: 20

## Operators

 Arithmetic Operators:

      3+2 #Addd
      4-1 #Substract
      2*3 #Multiply
      5/2 #Divide
      5**2 #Exponent

The += Operator:

 This is a convenient way to modify a variable. It takes the existing value in a variable and adds to it. You can also use any of the other mathematical operators e.g. -= or *=

      my_number = 4
      my_number += 2 
      #result is 6

The Modulo Operator:

 Often you'll want to know what is the remainder after a division. 
 e.g. 4 ÷ 2 = 2 with no remainder
 but 5 ÷ 2 = 2 with 1 remainder
 The modulo does not give you the result of the division, just the remainder.
 It can be really helpful in certain situations,
 e.g. figuring out if a number is odd or even.

       5 / 2
       #result is 1

      Float:

      5 / 3 == 1.6666666666666667 

      Integer:

      5 // 2 == 1

Logical Opperators:

and
 This expects both conditions either side of the and to be true.

      s = 58
      if s < 60 and s > 50:

      print("Your grade is C")

or

 This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.

      age = 12
      if age < 16 or age > 200:
      print("Can't drive")

not

  This will flip the original result of the condition. e.g. if it was true then it's now false.

      if not 3 > 1:
      print("something")
      #Will not be printed.

comparison operators

 These mathematical comparison operators allow you to refine your conditional checks.

      > Greater than
      < Lesser than
      >= Greater than or equal to
      <= Lesser than or equal to
      == Is equal to
      != Is not equal t

Identity Operators

      first_fruits_list = ["apple", "banana"]
      second_fruits_list = ["apple", "banana"]
      third_fruits_list = first_fruits_list

## Strings
Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.
### Basic String Operations:
1. Creating Strings:
You can create a string by enclosing text in single or double quotes:
   str1 = "Hello, world!"
   str2 = 'Python is fun!'
2. String Length: Use the len() function to get the length of a string:
    text = "Hello"
    print(len(text))  # Output: 5
3. Accessing Characters: You can access individual characters in a string using indexing:
    text = "Hello"
    print(text[0])  # Output: 'H' (first character)
    print(text[-1]) # Output: 'o' (last character)
4. split(delimiter): Splits the string into a list of substrings based on the delimiter.
    text = "Hello, world!"
    words = text.split(",")
    print(words)  # Output: ['Hello', ' world!']

### F-Strings (Formatted Strings):
Python provides a convenient way to format strings using f-strings (available in Python 3.6 and later). You can embed expressions inside curly braces {}:
    name = "Alice"
    age = 25
    greeting = f"Hello, my name is {name} and I am {age} years old."
    print(greeting)  # Output: 'Hello, my name is Alice and I am 25 years old.