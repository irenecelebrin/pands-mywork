# week 04, lab 2
# author: irene celebrin 

'''
Write a program (average.py) that keeps reading numbers until the user
enters a 0. (the program should append each of them into a list)
The program should then print out each of the numbers entered and the
average of them. (Use a list)

'''

import statistics

# create empty list 
numbers = []

# ask for a number 
number = int(input('enter number (0 to quit): '))

while number != 0: 
    numbers.append(number)
    number = int(input('enter number (0 to quit): '))

# print all numbers entered so far 
for number in numbers: 
    print(number)
    number =+ 1

# create average with statistics module, and round average to 2 decimal points
average = round(statistics.mean(numbers),0)

# create average dividing the sum of the numbers by the amount of elements in the list, and round to 2 decimal points 
average2 = round(float(sum(numbers) / len(numbers)),2)

#print average 
print(f'The average is {average2}')

