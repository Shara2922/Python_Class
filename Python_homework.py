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
company = len(company)
print(company)

# 6 Change all the characters to uppercase letters using upper() method.
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
company = company.find('Coding')
print(company)

# 11 Replace the word coding in the string 'Coding For All' to 'Python'.
company = company.replace('Coding', 'Python')
print(company)

# 12 Change Python For All to Python For Everyone using the replace method or other methods.
company = company.replace('All', 'Everyone')
print(company)

# 13 Split the string 'Coding For All' using space as the separator (split()) .
company = company.split(' ')
print(company)

# 14 "'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'" split the string at the comma.
company = company.split(',')
print(company)

# 15 What is the character at index 0 in the string 'Coding For All'.
company = company[0]
print(company)

# 16 What is the last index of the string 'Coding For All'.
company = company[-1]
print(company)

# 17 What character is at index 10 in 'Coding For All' string.
company = company[10]
print(company)

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = company[0:6]
print(company)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
company = company[0:6]
print(company)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
company = company.index('C')
print(company)

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
company = company.index('F')
print(company)
