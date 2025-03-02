# week 04, lab 2 
## author : irene celebrin 

# task 
# Write a program (guess1.py) that prompts the user to guess a number, the
#program should keep prompting the user to guess the number until the user
# gets the right on

# decide what's th number to guess 
number_to_guess = 11 
entered_number = int(input('Please guess a number: '))

while entered_number != number_to_guess: 
    print('Wrong')
    entered_number = int(input('Please guess again: '))
print(f'Well done! The number was {number_to_guess}')





