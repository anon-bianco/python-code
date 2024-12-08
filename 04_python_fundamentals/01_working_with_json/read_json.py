import json

with open(r"E:\coding\git_repo\python-code\04_python_fundamentals\01_working_with_json\book.txt", "r") as f:
  content = f.read()

print(type(content))

# Content from the txt file wil be read as a string.
# So, convert json_string to dictionry
# Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
content_dict = json.loads(content)

print(type(content_dict))

