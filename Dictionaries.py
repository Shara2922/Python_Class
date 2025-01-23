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
keys = student.keys()
print(keys)

# 8. Get the dictionary values as a list
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using items() method
items = student.items()
print(items)

# 10. Delete one of the items in the dictionary
del student['age']

# 11. Delete one of the dictionaries
del student