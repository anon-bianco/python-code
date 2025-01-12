list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate 2 lists
list3 = list1 + list2
print("Concatenate 2 lists")
print(list3)
print("\n")

# Concatenate 2 lists
list1.extend(list2)
print("Concatenate 2 lists using extend")
print(list1)
print("\n")

# Add an element at the beginning of the list
# Insert the element 100 at the 0th index
list1.insert(0, 100)
print("Add an element at the beginning of the list")
print(list1)
print("\n")

# Create a nested list
# Insert list2 within list1
print("Create a nested list")
list1.append(list2)
print(list1)
print("\n")

list2.append(4)

# Count the no of occurances of an element
print("Count the no of occurances of an element in list2")
print(f"list2 --> {list2}")
print(f"Element 4 count: {list2.count(4)}")
print(f"Element 5 count: {list2.count(5)}")
print(f"Element 1 count: {list2.count(1)}")
print("\n")

# Find the index of an element in a list
print("Find the index of an element in a list")
print(f"Index of value 5 is: {list2.index(5)}")
print("\n")

# Min and Max
print("Min and Max")
print(min(list2))
print(max(list2))
print("\n")

# Sort in ascending and descending order
print("Sort in ascending and descending order")
print("list2 -> ", list2)
list2.sort()
print("Ascending order: ", list2)
list2.sort(reverse=True)
print("Descending order: ", list2)
print("\n")


# Sum of list
print("Sum of list")
print(sum(list2))
print("\n")

# Remove an element based on index or last one
print("Remove an element based on index or last one")
print("list3 -> ", list3)
list3.pop()
print("Remove last element: ", list3)
list3.pop(2)
print("Remove element in index 2: ", list3)
print("\n")

# Remove an element based on the value
print("Remove an element based on the value")
print("list3 -> ", list3)
list3.remove(2)
print("Remove the value 2: ", list3)
print("\n")

# Clear all the elements in list
list1.clear()
print("Clear all the elements in list")
print(list1)
print("\n")

