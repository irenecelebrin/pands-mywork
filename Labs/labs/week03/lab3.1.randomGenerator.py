# week 03, lab 1 
# author: irene celebrin 

#  program that prints out a random number between 1 and 10


import random 

x = int(input('Enter the first number of the range: '))
y = int(input('Enter the second number of the range: '))
number = random.randint(x,y)
print('Here is a random number between {} and {}: {}'.format(x, y, number))


