# Homework : Strings

# 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2 Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
company = "Coding For All"
print(len(company))

# 6 Change all the characters to uppercase letters using upper() method.
company = "Coding For All"
company = company.upper()
print(company)

# 7 Change all the characters to lowercase letters using lower() method.
company = company.lower()
print(company)

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)

# 9 Cut(slice) out the first word of Coding For All string.
company = company[6:]
print(company)

# 10 Check if Coding For All string contains a word Coding using the method index(), find() or other methods.
text = "Coding For All"
word = "Coding"

# Using find() to check if 'Coding' exists
position = text.find(word)

if position != -1:
    print(f"The word '{word}' is found at index {position}.")
else:
    print(f"The word '{word}' is not found.")


# 11 Replace the word coding in the string 'Coding For All' to 'Python'.
company = "Coding For All"
company = company.replace('Coding','Python')
print(company)

# 12 Change Python For All to Python For Everyone using the replace method or other methods.
company = company.replace('All', 'Everyone')
print(company)

# 13 Split the string 'Coding For All' using space as the separator (split()) .
company = company.split(' ')
print(company)

# 14 "'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'" split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company = company.split(',')
print(company)

# 15 What is the character at index 0 in the string 'Coding For All'.
company = company[0]
print(company)

# 16 What is the last index of the string 'Coding For All'.
company = company[-1]
print(company)

# 17 What character is at index 10 in 'Coding For All' string.
text = "Coding For All"

# Get the character at index 10
character = text[10]
print(f"The character at index 10 is: '{character}'")

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = company[0:6]
print(company)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
company = company[0:6]
print(company)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"

# Find the position of the first occurrence of 'C'
position = text.index('C')
print(f"The position of the first occurrence of 'C' is: {position}")

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All"

# Find the position of the first occurrence of 'F'
position = text.index('F')
print(f"The position of the first occurrence of 'F' is: {position}")

# Homework : Lists

# 1. Declare an empty list
list =[]

# 2. Declare a list with more than 5 items
list =["apple", "banana", "cherry", "orange", "mango", "lemon"]

# 3. Find the length of your list
list =["apple", "banana", "cherry"]
print(len(list))

# 4. Get the first item, the middle item and the last item of the list
list = ["apple", "banana", "cherry", "mango", "lemon"]

# First item
print(list[0])  # Output: "apple"

# Middle item
print(list[len(list)//2])  # Output: "cherry"

# Last item
print(list[-1])  # Output: "lemon"


# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types =["name", "age", "height", "marital status", "address"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 8. Print the number of companies in the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
number_of_companies = len(it_companies)
print(f"The number of companies in the list is: {number_of_companies}")

# 9. Print the first, middle and last company
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 10. Print the list after modifying one of the companies
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies [0] = "Twitter"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies  =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("IT company")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(3, "IT company")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = '#; '.join(it_companies)
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Apple" in it_companies)

# 16. Sort the list using sort() method
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.sort()
it_companies.reverse()
print("Reversed list in descending order:", it_companies)

# 18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("First 3 companies:", first_three_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Last 3 companies:", last_three_companies)

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 1: 
    middle_companies = it_companies[middle_index:middle_index+1]
else:  
    middle_companies = it_companies[middle_index-1:middle_index+1]

print("Middle company(ies):", middle_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0) 
print("Updated list:", it_companies)

# 22. Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 1:  
    it_companies.pop(middle_index)
else:
    it_companies.pop(middle_index)  
    it_companies.pop(middle_index - 1)  

print("Updated list:", it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print("Updated list:", it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print("Updated list:", it_companies)

# 25 Destroy the IT companies list
del it_companies
try:
    print(it_companies)
except NameError:
    print("The list has been destroyed.")

# 26. Join the following lists: front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'], back_end = ['Node.js', 'Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node.js', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Full stack:", full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack_copy=full_stack.copy()
print(full_stack_copy)
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

# Homework Tuple :

# 1. Create an empty tuple.
empty_tuple = ()

# 2. Create tuples for sisters and brothers.
sisters = ("Anna", "Bella")
brothers = ("Chris", "David")

# 3. Join brothers and sisters tuples.
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. Count the number of siblings.
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Add parents to the siblings tuple.
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)

# Homework : Sets

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Cisco', 'SAP'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)

# 5. What is the difference between remove and discard
# remove() will raise an error if the element does not exist in the set, while discard() will not raise an error.
it_companies.discard('Apple')
print(it_companies)

# 6. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.union(B)
print(A)

# 7. Find A intersection B
A.intersection(B)
print(A)

# 8. Is A subset of B
A.issubset(B)
print(A)

# 9. Are A and B disjoint sets
A.isdisjoint(B)
print(A)

# 10. Join A with B and B with A
A.union(B)
B.union(A)
print(A)

# 11. What is the symmetric difference between A and B
A.symmetric_difference(B)
print(A)

# 12. Delete the sets completely
del A
del B

# Homework : Dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Doggy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 5
}

# 3. Create a student dictionary and add first_name, last_name, age, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Shara',
    'last_name': 'Rahman',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'HTML', 'CSS'],
    'country': 'Finland',
    'city': 'Helsinki',
    'address': {
        'street': 'Highland',
        'zipcode': '77530'
    }
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['React', 'Node.js'])
print(student['skills'])

# 7. Get the dictionary keys as a list
student = {"name": "Shara", "age": 30, "grade": "A"}
keys = list(student.keys())
print(keys)

# 8. Get the dictionary values as a list
values = list(student.values())
print(values)

# 9. Change the dictionary to a list of tuples using items() method
items = list(student.items())
print(items)

# 10. Delete one of the items in the dictionary
del student['address']

# 11. Delete one of the dictionaries
del student
