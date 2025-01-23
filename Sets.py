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

# Homework Tuple : A tuple is a collection of different data types which is ordered and unchangeable (immutable).

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