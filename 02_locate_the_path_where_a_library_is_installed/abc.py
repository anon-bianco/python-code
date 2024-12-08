# type: ignore

def main():
  print('This is Anon Bianco')

if __name__ == "__main__":
   main()

import fastapi

file_path = fastapi.__file__
print(file_path)