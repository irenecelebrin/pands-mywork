# week 6, lab 6 
# author: irene celebrin 


# function to display the command menu and prompt the user to pick a command
def displayMenu(): 
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit ')
    choice = input('Type one letter (a/v/q): ').strip()
    
    return choice


# function to read in student name and modules, ot be executed if user picks option a. it create a dict. and store values in the student list 
def do_add(students): 
    current_student = {}
    current_student['name'] = input('Please enter student name: ')
    current_student['modules'] = read_modules()
    
    students.append(current_student)

# function to read in modules and grades 
def read_modules():

    #create empty list for dict with module and grade 
    modules = []
    module_name = input('Enter the first module name (blank to quit): ').strip()

    while module_name != '':
        # create dict with pair module-grade 
        current_module = {}
        current_module['name'] = module_name
        current_module['grade'] = int(input('Enter grade: '))

        #append dict to the list 
        modules.append(current_module)
        # ask for another module and grade 
        module_name = input('enter the next module name (blank to quit) : ').strip()

    #return full list of modules and grades 
    return modules 

# function to display modules and grades for each student 

# function to be executed if user picks v 
def do_view(students):
    for student in students:
        print(f'student name: {student['name']}')
        for module in student['modules']:
            print(f'\tmodule: {module['name']}\t\t grade: {module['grade']}')
    

# main program: 
#create empty list to include student dictionaries 
students = []
choice = displayMenu()

while choice != 'q':
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice != 'q':
        print(f"\nplease select either a,v or q")
    choice = displayMenu()



