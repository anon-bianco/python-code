emp_01 = {
    'first_name': 'Anon',
    'last_name': 'Bianco',
    'age': 25
}

print(emp_01)
print()

print(emp_01['first_name'])
print()

# Print only the values of each key
print(emp_01.values())
print()

# Print both key and value 
print(emp_01.items())
print()

# Insert a new element into an existing dictionary
emp_01['ph_no'] = 9489589584
print(emp_01)
print()

# Update the value in an existing key
emp_01['age'] = 26
print(emp_01)
print()

# Remove an element based on key
emp_01.pop('age')
print(emp_01)
print()

# Delete all elements in a dictionary
emp_01.clear()
print(emp_01)
print()

# Create an empty dictionary
emp_02 = dict()
print(emp_02)