# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i, end=" ")
print()
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
print()
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i, end=" ")
print()
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1
print()

# 3. Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 4. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print()
# 5. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum += i
print("Sum of all numbers from 0 to 100 is:", sum)
# 6. Use for loop to iterate from 0 to 100 and print the sum of all even numbers.
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print("Sum of all even numbers from 0 to 100 is:", sum)
