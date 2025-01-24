# Conditionals Exercises: Day 9
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.Output:Enter your age: 30.You are old enough to learn to drive.
# Output:Enter your age: 15. You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. \
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30. You are 5 years older than me.

my_age = 30
your_age = int(input("Enter your age : "))
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age!")
# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
# Level 2: 1 . Write a code which gives grade to students according to theirs scores: A 80-100,B 70-89,C 60-69,D 50-59,F 0-49

score = float(input("Enter the student's score (0-100): "))

if score > 100 or score < 0:
    print("Invalid score")
elif score >= 80:
    print("The student's grade is: A")
elif score >= 70:
    print("The student's grade is: B")
elif score >= 60:
    print("The student's grade is: C")
elif score >= 50:
    print("The student's grade is: D")
else:
    print("The student's grade is: F")

# 2 . Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer

month = input("Enter the month : ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month. Please enter a valid month.")

# 4 . The following list contains some fruits: fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the name of a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Updated list of fruits:", fruits)

# Level 3 : Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
     skills = person['skills']
     middle_index = len(skills) // 2
     print("Middle skill:", skills[middle_index])

 # 2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
has_python = 'Python' in skills
print("Has Python skill:", has_python)

 # 3. If a person skills has only JavaScript and React, print('He is a front end developer'),
 # if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
 # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
 # - for more accurate results more conditions can be nested!
if skills == ['JavaScript', 'React']:
     print("He is a front end developer")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
     print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
     print("He is a fullstack developer")
else:
     print("Unknown title")

 # 4. If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] and person['country'] == 'Finland':
     print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
