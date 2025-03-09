# week 06, lab 4 
# author : irene celebrin 

#task 
'''
We can now write the function doAdd(students). So we need to think what 
we want this to do.
a. Read in the student’s name (that is straightforward)
b. Read in the module names and grades (this is a bit more complicated 
so let’s put this in separate function and think about it by itself, see 5. 
below)
c. Test this function, it creates a student dict, we can print that out.
d. We should add the student dict to list (pass this list in)
e. Test this.
'''

#create empty list to include student dictionaries 
students = []

# function to read in modules 
def read_modules():
    return []

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

