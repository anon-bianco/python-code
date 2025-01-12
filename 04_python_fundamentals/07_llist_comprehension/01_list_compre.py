# Find odd numbers from lst and add to lst2
lst = [1, 2, 3, 4, 5, 6]

lst2 = list()

for i in lst:
  if i%2 == 1:
    lst2.append(i)

print(lst2)    
print()

# Simplify the program with list comprehension
lst3 = [i for i in lst if i%2==1]
print(lst3)