import json

book = {}

book['anon'] = {
  'name': 'Anon Bianco',
  'address': 'Bians Niche, South of Amala Convent',
  'phone': 9489589584
}

book['anne'] = {
  'name': 'Anne Biancy',
  'address': 'Bians Niche, South of Amala Convent',
  'phone': 9361607439
}

# Converts python dictionary into a string
# dictionary will be converted into json
json_string = json.dumps(book, indent=4)
print(type(json_string))
print(json_string)

# Save it to a text file
with open(r"E:\coding\git_repo\python-code\04_python_fundamentals\01_working_with_json\book.txt", "w") as f:
  f.write(json_string)