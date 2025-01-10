# Recursive function

# Eg: 5+4+3+2+1 = 15

def sum_of_n(n):
    # Base case
    if(n==1):
        return 1

    # Recursive case
    return n + sum_of_n(n-1)

print(sum_of_n(5))




# Factorial program with recursion
def factorial(n):
    if(n==1):
        return 1

    return n * factorial(n-1)

print(factorial(4))  
