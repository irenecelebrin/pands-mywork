# week 04, lab 1 
## author: icelebrin 

# task: Write a program (isEven.py) that asks the user to enter in a number, and the program will tell the user if the number is even or odd.


# ask user to provide a number 
number = int(input('Enter a number: '))

# check number 
if (number % 2) == 0: 
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')


