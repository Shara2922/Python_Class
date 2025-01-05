# Print

print("Hello World!")

#Input function

name = input("What is your name?")
print("Hello " + name)

# Naming Conversion:
# Camel Case: myVariableName
# Snake Case: my_vartiable_name

# Arithmetic Operators:

# Addition: 
assert 5 +3 == 8
# Subtraction:
assert 5 - 3 == 2
# Multiplication:
assert 5 * 3 == 15
# Division :
assert 5 / 3 == 1.6666666666666667
assert isinstance(5 / 3, float)

 # Floor division:
assert 5 // 3 == 1
assert isinstance(5 // 3, int)

# Exponentiation:
assert 5 ** 3 == 125
assert isinstance(5 ** 3, int)

# Bitwise operators:
 # AND
    # 1 if both bits aren 1.

# OR
    # 1 if one of the bits is 1. 

# NOT
    # Inverts all the bits.

# XOR
    # 1 if the bits are different.

# Signed right shift:
# Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits
# fall off.
    # Example:
    # 5 = 0b0101
assert 5 >> 1 == 2  # 0b0010
assert 5 >> 2 == 1  # 0b0001

# Left shift:
# Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    # Example:
    # 5 = 0b0101
assert 5 << 1 == 10  # 0b1010
assert 5 << 2 == 20  # 0b10100

# Zero fill left shift
# Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    # Example:
    # 5 = 0b0101
assert 5 << 1 == 10  # 0b1010
assert 5 << 2 == 20  # 0b10100

# Assignment Operators (=, +=, -=, /=, //= etc.)
number = 5
assert number == 5
number += 3
assert number == 8
number -= 3
assert number == 5
number *= 3
assert number == 15
number /= 3
assert number == 5.0
number //= 3
assert number == 1
number **= 3
assert number == 1

# Comparison Operator (==, !=, >, <, >=, <=)
assert 5 > 3  # Greater than
assert 3 < 5  # Lesser than
assert 5 >= 3  # Greater than or equal to
assert 3 <= 5  # Lesser than or equal to
assert 5 == 5  # Is equal to
assert 5 != 3  # Is not equal to

# Logical Operators (and, or, not)
assert 5 > 3  # This is True
assert 5 > 3 or 5 < 3  # or
assert not (5 < 3)  # This ensures 5 is not less than 3

# Identity Operators (is, is not)
assert 5 is 5
assert 5 is not 3

# Membership Operators (in, not in)
assert 5 in [1, 2, 3, 4, 5]
assert 5 not in [1, 2, 3, 4]
