# week 04, lab 2
# author: irene celebrin 

#Task 
# How would you modify the program in 3 (guess2.py) above, so that the program tells the user if there guess is too high or too low, each time they guess. 
# HINT: put an if statement inside the while loop

import random 

# decide a number 
my_number = 11

# generate random number between 0 and 100
rand_number_to_guess = random.randint(0,100)

#ask user for a number 
entered_number = int(input('Please guess a number: '))

#create while loop to print wrong and ask for the number until the user guesses
while entered_number != rand_number_to_guess: 
    if entered_number < rand_number_to_guess:
        print('too low')
        entered_number = int(input('Please guess again: '))
    else: 
        print('too high')
        entered_number = int(input('Please guess again: '))
print(f'Well done! Yes the number was {rand_number_to_guess}')




    