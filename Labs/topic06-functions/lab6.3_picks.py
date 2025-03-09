# week 06, lab 3
# author: irene celebrin

# task: We will now use that function. Create a program that keeps displaying the 
# menu until the user picks q. if the user chooses a then call a function called 
# doAdd() if the user chooses v then call a function called doView().
# (I copied the function from the last function into this program)

# function to display the command menu and prompt the user to pick a command
def displayMenu(): 
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit ')
    choice = input('Type one letter (a/v/q): ').strip()
    
    return choice

# function to add a student, to be exectuted if user picks a 
def doAdd():
    print('in adding')

# function to be executed if user picks v 
def doView():
    print('in viewing')



choice = displayMenu()

while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print(f'"\nplease select either a,v or q"')
    choice = displayMenu()



