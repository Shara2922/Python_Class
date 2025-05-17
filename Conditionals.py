#Conditionals Practice
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive. Output:
 #Enter your age: 15 . You need 3 more years to learn to drive.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year(s) to learn to drive.")

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30 . You are 5 years older than me.

my_age = 25  # You can set this to any age you like
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age!")

# 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4 . Enter number two: 3 . 4 is greater than 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# 4. Write a code which gives grade to students according to theirs scores:
# 80-100, A ; 70-89, B ; 60-69, C; 50-59, D; 0-49, F
def get_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid score'

# Example usage:
scores = [95, 72, 67, 58, 40, -5, 105]

for s in scores:
    print(f"Score: {s} => Grade: {get_grade(s)}")
