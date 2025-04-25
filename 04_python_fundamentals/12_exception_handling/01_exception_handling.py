# Basic exception handling
try:
    # Code that might raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# ***************************************************

# Handling multiple exceptions
try:
    file = open("nonexistent.txt")
    content = file.read()
    number = int(content)
except FileNotFoundError:
    print("File doesn't exist")
except ValueError:
    print("File content is not a valid number")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# ***************************************************
# Try-Except-Else-Finally

try:
    file = open("example.txt", "w")
    file.write("Hello World")
except IOError:
    print("Error writing to file")
else:
    print("File written successfully")  # Executes if no exception occurs
finally:
    file.close()  # Always executes, regardless of exceptions
    print("File closed")

# ***************************************************
# Custom Exceptions:

class AgeError(Exception):
    """Custom exception for invalid age"""
    pass

def verify_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age > 150:
        raise AgeError("Age seems invalid")
    return f"Age {age} is valid"

try:
    result = verify_age(-5)
    print(result)
except AgeError as e:
    print(f"Invalid age: {e}")
# ***************************************************
# Context Managers (with statement):

def process_file(filename):
    try:
        with open(filename, 'r') as file:  # File automatically closes after with block
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File {filename} not found")
    except IOError as e:
        print(f"Error reading file: {e}")

process_file("abc")