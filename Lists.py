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
