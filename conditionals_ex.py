# Conditionals Exercises: Day 9

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. \
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

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