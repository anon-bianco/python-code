# Can have any datatypes
set1 = {1, 2, "Anon", 4, 5}

print(type(set1))

# Doesn't allow duplicate elements
set2 = {1, 1, 2, 2, 3}
print(set2)

# Set is unordered
# Let's try adding an element
set2.add(67)
set2.add(9)
print(set2)

# Remove an element by directly passing the value itself
set2.remove(1)
print(set2)

# Add boolean in set
set2.add(False)
print(set2)
print()

# Delete all elements in a set
print(set1)
set1.clear()
print(set1)
print()

# Convert list to set
list1 = [1, 55, 89, "Hello"]
print(list1)
print(type(list1))
set3 = set(list1)
print(set3)
print(type(set3))
print()

# Set operations
set4 = {2, 3, 4}
set5 = {1, 4, 5}

print(set4.union(set5))
print(set4.intersection(set5))
print(set4.difference(set5))
print()

# Iterate a set
for i in set3:
  print(i)
print()

# Membership operator to check whether an element is present in a set or not 
print(1 in set4)
print(4 in set4)
print()