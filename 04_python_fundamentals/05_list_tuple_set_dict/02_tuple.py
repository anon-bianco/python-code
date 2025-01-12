nums = (5, 6, 1, 100, 20, 6)

# length
print("Find length")
print(len(nums))
print("\n")

# min and max
print("min: ", min(nums))
print("max: ", max(nums))
print("\n")

# Find the no of occurances of a value
print("No of occurances of 6 is: ", nums.count(6))
print("\n")

# Find index position of an element
print("Index position of 100 is: ", nums.index(100))
print("\n ")

# Convert tuple to list
print("Convert tuple to list")
nums = list(nums)
print(type(nums))
