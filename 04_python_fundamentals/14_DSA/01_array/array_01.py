stock_prices = [298, 305, 320, 301, 292]

# Q2: On what day price was 301?
#  O(n)

def day_price_301():
    for i in range(len(stock_prices)):
        if stock_prices[i] == 301:
            return i

# q2 = day_price_301()        
# print(q2)

# Q4: Insert new price 284 at index 1
# O(n)

# stock_prices.insert(1, 284)
# print(stock_prices)

# Monthly expense problem

monthly_expense = [2200, 2350, 2600, 2130, 2190]


# P1: In feb how many dollars you spent extra compare to jan

def p1():
    return monthly_expense[1] - monthly_expense[0]

# extra_spent = p1()
# print(extra_spent)

# P2: Find out total expense in quarter 1
def p2():
    return monthly_expense[0] + monthly_expense[1] + monthly_expense[2]

# q1_expense = p2()
# print(q1_expense)

# P3: Find out if you spent exactly 2000 dollars in any month


def p3():
    for i in range(len(monthly_expense)):
        if monthly_expense[i] == 2000:
            return i

# month_usd_2000 = p3() 
# print(month_usd_2000)       

# P4: June expense 1980, add to list

# monthly_expense.append(1980)
# print(monthly_expense)

# P5: 

# print(monthly_expense)
# monthly_expense[3] = monthly_expense[3] - 200
# print(monthly_expense)


# Exercise 2: Super hero
heros=['spider man','thor','hulk','iron man','captain america']


# P1: Length of the list
print(len(heros))

# P2: Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
print()


# P3: You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.pop()
print(heros)
heros.insert(3, 'black panther')
print(heros)
print()

# P4: 
heros[1: 3] = ['doctor strange']
print(heros)
print()

# P5:

heros.sort()
print(heros)