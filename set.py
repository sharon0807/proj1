# Creating sets
s = {1, 2, "apple", True, 2}
print(s, type(s))

# Creating empty sets
empty_set = set()
print(type(empty_set))

# Getting the length of a set
print(len(s))

# Adding and removing elements from a set
my_set = {1, 2, 3, 7, 3}
my_set.add(9)
my_set.remove(3)
print(my_set)
my_set.discard(10)
print(my_set)
print(my_set.pop())  # Pop removes an arbitrary element
print(my_set)

# Adding a tuple to a set
my_set.add((1, 2, 3))
print(my_set)

# Clearing a set
my_set.clear()
print(my_set)

# Creating new sets
set1 = {1, 2, 3, 4}
set2 = {"banana", "apple", 2}

# Union of sets
print(set1.union(set2))
print(set2.union({"banana", "grape"}))
print(set2.union(("banana", "grape")))  # Convert tuple to set for union
print(set1 | set2 | s)  # Using bitwise OR operator for union

# Updating a set with another set
set1.update(set2)
print(set1)
set1 |= set2  # Equivalent to update
print(set1)

# Intersection of sets
print(set2.intersection(set1, s))
print(set2 & set1)

# Updating a set with intersection
set1.intersection_update(set2)
print(set1)
set2.intersection_update(["banana", "grape"])
print(set2)

# Difference of sets
print(set1.difference(set2))
print(set2 - set1)

# Updating a set with difference
set3 = {"pear", 1}
print(set3.difference_update({"pear"}))

# Symmetric difference of sets
print(set1.symmetric_difference(set2)) # you cant pass here 2 argument union or intersection
print(set2 ^ set1 ^set3)

# Updating a set with symmetric difference 
print(set1.symmetric_difference_update(set2))

result_set = set1.symmetric_difference(set2).symmetric_difference(set3)
print(result_set)

set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Check if the sets are disjoint
disjoint = set1.isdisjoint(set2)

print(disjoint)  # Output: True
A = {1, 2}
B = {1, 2, 3}

# Check if A is a subset of B
subset = A.issubset(B)
print("A is a subset of B:", subset) 
print(A.issubset(("siva")))
print(A<=A)

# Check if B is a superset of A
superset = A.issuperset(B)
print("B is a superset of A:", superset) 
print(A>=A)
A.clear()
print(A)
del A
print(A)
