# week04, lab 1 
## author: irene celebrin 

# task How would you use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1


'''1 was: 
Write a program (isEven.py) that asks the user to enter in a number, and the
program will tell the user if the number is even or odd.'''


# ask user to provide a number 
number = int(input('Enter a number: '))

# check number 
while number != -1:
    if (number % 2) == 0: 
        print(f'{number} is an even number')
        number = int(input('Enter a number: '))
    else:
        print(f'{number} is an odd number')
        number = int(input('Enter a number: '))

    

