# Week 03, lab 1
# author: irene celebrin


# write a program (div.py) that reads in two numbers and divides the first one by the second and give the integer result and the remainder.

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

result = x / y
int_result = int(x / y)
remainder = result - int_result



print('{} divided by {} is {} with remainder {}'.format(x, y, int_result, remainder))


# alternative solution 
'''
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by y {} is {} with remainder {}".format( x, y,
answer, remainder))

'''