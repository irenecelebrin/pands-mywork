# week 06, lab 5 
# author: irene celebrin 

# task We can now think about how to read in the modules. We want to keep 
# reading modules until the user enters a module name of blank. 


#create empty list to include student dictionaries 
students = []

# function to read in modules and grades 
def read_modules():

    #create empty list for dict with module and grade 
    modules = []
    module_name = input('Enter the first module name (blank to quit): ')

    while module_name != '':
        # create dict with pair module-grade 
        current_module = {}
        current_module['name'] = module_name
        current_module['grade'] = input('Enter grade: ')

        #append dict to the list 
        modules.append(current_module)
        # ask for another module and grade 
        module_name = input('enter the next module name (blank to quit) : ')

    #return full list of modules and grades 
    return modules 

# function to read in student name and modules, create a dict. and store values in the student list 
def do_add(students): 
    current_student = {}
    current_student['name'] = input('Please enter student name: ')
    current_student['modules'] = read_modules()
    
    students.append(current_student)

#test   
do_add(students)
do_add(students)

print(students)

