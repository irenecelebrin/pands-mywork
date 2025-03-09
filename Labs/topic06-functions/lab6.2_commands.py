# week 06, lab 2
# author: irene celebrin 

# Task: Write a function that prints out a menu of commands we can perform, ie add, 
# view and quit. The function should return what the user chose.
# Test the function. We don’t need to worry about error handling yet


def displayMenu(): 
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit ')
    choice = input('Type one letter (a/v/q): ').strip()
    
    return choice

choice = displayMenu()
print(f'You chose {choice}')