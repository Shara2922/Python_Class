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
- [Lists](#lists)
- [Tuples](#tuple)
- [Dictionaries](#dictionaries)
- [Python Homework](https://github.com/Shara2922/Python_Class/blob/main/Python_homework.py)

## Key Features of Python:
 * Easy to Learn: Python has a clean and straightforward syntax, making it beginner friendly.
 
 * Interpreted Language: Code is executed line by line, which makes debugging easier.
 
 * Dynamically Typed: You don’t need to declare the type of a variable.
 
 * Versatile: Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
 
 * Extensive Libraries: It has a vast standard library and many third-party libraries for specialized tasks.

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

      if height >= 120
      print("You can ride the rollercoaster")
      else:
      print("Sorry you have to grow taller to ride the rollercoaster")

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

## Operators :

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

## Strings :
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

## Lists :
There are four collection data types in Python :
 * List is a collection which is ordered and changeable(modifiable). Allows duplicate members.
 * Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
 * Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed
 * Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
 
 A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

### Basic List Operations:
1. Creating a List :

       my_list = [1, 2, 3, 4, 5]

2. Accessing Elements :
 * Indexing: Access specific elements using their index (starting from 0)

       print(my_list[0])  # Output: 1
       print(my_list[-1]) # Output: 5 (last element)

 * Slicing: Extract a portion of the list.

       print(my_list[1:4]) # Output: [2, 3, 4]
       print(my_list[:3])  # Output: [1, 2, 3]

3. Modifying a List :
 * Append: Add an element to the end

       my_list.append(6) # my_list = [1, 2, 3, 4, 5, 6]
 * Extend: Add multiple elements

       my_list.extend([7, 8]) # my_list = [1, 2, 3, 4, 5, 6, 7, 8]
 * Insert: Add an element at a specific index

       my_list.insert(2, 99) # my_list = [1, 2, 99, 3, 4, 5]
4. Removing Elements :
 * Remove: Remove the first occurrence of a value

       my_list.remove(99) # my_list = [1, 2, 3, 4, 5]
 * Pop: Remove and return an element at a specific index.

       my_list.pop(2) # Removes and returns 3, my_list = [1, 2, 4, 5]
 * Clear: Remove all elements.

       my_list.clear() # my_list = []

5. Other Common Operations
 * Length: Get the number of elements.

       print(len(my_list)) # Output: 5

 * Check Membership: Check if an item exists.

       print(3 in my_list)  # Output: True
       print(10 in my_list) # Output: False

 * Concatenation: Combine two lists.

       new_list = my_list + [6, 7, 8]

 * Repetition: Repeat a list multiple times.

       repeated_list = my_list * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

6. Sorting and Reversing
 * Sort: Sort elements in ascending order.

       my_list.sort()  # Modifies the list in place
 * Reverse Sort: Sort in descending order.

       my_list.sort(reverse=True)
 * Reverse: Reverse the order of the list.

       my_list.reverse()
7. Copying a List
Shallow Copy: Create a copy of the list.

       new_list = my_list.copy()
8. List Comprehension
Create a new list based on existing elements.

       squares = [x**2 for x in my_list if x % 2 == 0]

## Tuples :
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

 * tuple(): to create an empty tuple
 * count(): to count the number of a specified item in a tuple
 * index(): to find the index of a specified item in a tuple

### Basic Tuple Operations:
 
1. Creating a Tuple
 * With parentheses

       my_tuple = (1, 2, 3, 4, 5)

 * Single-element tuple (requires a trailing comma)

       single_element_tuple = (42,)

 * Empty tuple

       empty_tuple = ()
2. Accessing Elements
 * Indexing: Access elements using their index (starting at 0).

       print(my_tuple[0])  # Output: 1
       print(my_tuple[-1]) # Output: 5 (last element)
 * Slicing: Extract a portion of the tuple.

       print(my_tuple[1:4]) # Output: (2, 3, 4)
       print(my_tuple[:3])  # Output: (1, 2, 3)
3. Operations with Tuples
 * Concatenation: Combine two tuples.

       new_tuple = my_tuple + (6, 7, 8)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
 * Repetition: Repeat a tuple multiple times.

       repeated_tuple = my_tuple * 2  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
 * Membership Test: Check if an item exists in the tuple.

       print(3 in my_tuple)  # Output: True
       print(10 in my_tuple) # Output: False
 * Length: Get the number of elements.

       print(len(my_tuple))  # Output: 5
4. Tuple Unpacking
 * Assign values in a tuple to variables.

       a, b, c = (1, 2, 3)
       print(a, b, c)  # Output: 1 2 3
 * Use * to capture remaining elements.

       a, *b = (1, 2, 3, 4, 5)
       print(a)  # Output: 1
       print(b)  # Output: [2, 3, 4, 5]
5. Tuple Methods
 * Count: Count the occurrences of an element.

       print(my_tuple.count(2))  # Output: 1
 * Index: Find the first index of an element.

       print(my_tuple.index(3))  # Output: 2
6. Iterating Over a Tuple
 * Use a loop to iterate through elements.

       for item in my_tuple:
       print(item)
7. Nested Tuples
Tuples can contain other tuples.

       nested_tuple = (1, (2, 3), (4, 5, 6))
       print(nested_tuple[1])       # Output: (2, 3)
       print(nested_tuple[1][0])    # Output: 2
8. Converting Between Lists and Tuples
 * Convert Tuple to List: To modify elements.

       my_list = list(my_tuple)
 * Convert List to Tuple: For immutability.

       my_tuple = tuple(my_list)
## Sets :
In Python, sets are unordered collections of unique elements. They support various operations, particularly those used in mathematical set theory. Here's an overview of basic set operations:
### Basic Set Operations :
1. Creating a Set
 * Creating a set with unique elements

       my_set = {1, 2, 3, 4, 5}
 * Creating an empty set (must use set(), not {})

       empty_set = set()

 * Using set() to create a set from an iterable

       my_set = set([1, 2, 2, 3, 4])  # Output: {1, 2, 3, 4}
2. Adding and Removing Elements
 * Add: Add a single element.

       my_set.add(6)  # my_set = {1, 2, 3, 4, 5, 6}
 * Update: Add multiple elements (can be a list, tuple, or another set)

       my_set.update([7, 8])  # my_set = {1, 2, 3, 4, 5, 6, 7, 8}
 * Remove: Remove an element (raises an error if not found).

       my_set.remove(3)  # my_set = {1, 2, 4, 5, 6, 7, 8}
 * Discard: Remove an element (does not raise an error if not found)

       my_set.discard(9)  # Safe removal
 * Pop: Remove and return a random element.

       element = my_set.pop()  # Removes an arbitrary element
 * Clear: Remove all elements.

       my_set.clear()  # my_set = set()
3. Set Operations
 * Union : Combine all elements from two sets.

       set1 = {1, 2, 3}
       set2 = {3, 4, 5}
       union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}
      Or use |:

       union_set = set1 | set2
 * Intersection : Get common elements between sets.

       intersection_set = set1.intersection(set2)  # Output: {3}
      Or use &:

       intersection_set = set1 & set2
 * Difference : Get elements in one set but not in the other.

       difference_set = set1.difference(set2)  # Output: {1, 2}
      Or use -:

       difference_set = set1 - set2
 * Symmetric Differenc : Get elements in either set but not both.

       symmetric_difference_set = set1.symmetric_difference(set2)  # Output: {1, 2, 4, 5}
      Or use ^:

       symmetric_difference_set = set1 ^ set2
4. Subset, Superset, and Disjoint
 * Subset: Check if one set is a subset of another.

       set1 = {1, 2}
       set2 = {1, 2, 3}
       print(set1.issubset(set2))  # Output: True
 * Superset: Check if one set is a superset of another.

       print(set2.issuperset(set1))  # Output: True
 * Disjoint: Check if two sets have no elements in common.

       set3 = {4, 5}
       print(set1.isdisjoint(set3))  # Output: True
5. Other Operations
 * Length: Get the number of elements.

       print(len(my_set))  # Output: 5
 * Membership Test: Check if an element is in the set.

       print(3 in my_set)  # Output: True
       print(10 in my_set) # Output: False
6. Converting Between Sets and Other Types
 * Convert to List/Tuple:

       my_list = list(my_set)
       my_tuple = tuple(my_set)
 * Convert from List/Tuple:

        new_set = set([1, 2, 3, 4, 4])  # Output: {1, 2, 3, 4}
7. Iterating Over a Set

       for item in my_set: 

       print(item)

## Dictionaries :
  In Python, dictionaries are collections of key-value pairs, where keys are unique, and values can be of any type. Here's an overview of basic dictionary operations:
1. Creating a Dictionary
 * Using curly braces

       my_dict = {"name": "Alice", "age": 25, "city": "New York"}

 * Using the dict() function

       my_dict = dict(name="Alice", age=25, city="New York")

 * Empty dictionary

       empty_dict = {}
2. Accessing Elements
 * Access by Key: Use the key to get the corresponding value.

       print(my_dict["name"])  # Output: Alice
 * Using get(): Returns None or a default value if the key doesn't exist.

       print(my_dict.get("age"))       # Output: 25
       print(my_dict.get("salary", 0)) # Output: 0
3. Adding and Updating Elements
 * Add a New Key-Value Pair:

       my_dict["salary"] = 50000  # {"name": "Alice", "age": 25, "city": "New York", "salary": 50000}
 * Update an Existing Key:

       my_dict["age"] = 30  # {"name": "Alice", "age": 30, "city": "New York", "salary": 50000}
4. Removing Elements
 * pop(): Remove a key and return its value.

       salary = my_dict.pop("salary")  # salary = 50000, my_dict = {"name": "Alice", "age": 30, "city": "New York"}
 * popitem(): Remove and return the last key-value pair (arbitrary in older versions).

       last_item = my_dict.popitem()  # Output: ("city", "New York")
 * del: Delete a key-value pair.

       del my_dict["age"]  # {"name": "Alice"}
 * clear(): Remove all elements.

       my_dict.clear()  # {}
5. Iterating Through a Dictionary
 * Keys:
   for key in my_dict:

       print(key)
 * Values:
   for value in my_dict.values():

       print(value)
 * Key-Value Pairs:
   for key, value in my_dict.items():

       print(f"{key}: {value}")
6. Dictionary Methods
 * keys(): Get all keys.

       print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
 * values(): Get all values.

       print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])
 * items(): Get all key-value pairs as tuples.

       print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
 * update(): Merge another dictionary into the current one.

       my_dict.update({"profession": "Engineer", "age": 35})
7. Membership Testing
 * Check Key Existence:

       print("name" in my_dict)  # Output: True
       print("salary" in my_dict)  # Output: False
8. Dictionary Comprehension
 * Create a dictionary from an iterable or condition.

       squares = {x: x**2 for x in range(1, 6)}
       
       Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
9. Copying a Dictionary
 * Shallow Copy:

       new_dict = my_dict.copy()
 * Deep Copy: Use copy module for nested dictionaries.

       import copy
       deep_copy = copy.deepcopy(my_dict)
10. Nested Dictionaries
 * Dictionaries can contain other dictionaries.

       nested_dict = {
           "person1": {"name": "Alice", "age": 25},
           "person2": {"name": "Bob", "age": 30}
       }
       print(nested_dict["person1"]["name"])  # Output: Alice