# week 05, lab 1 
# author: icelebrin 

'''If you want to go a step further, read in multiple students (until the
student_name is blank.
Next week we will be looking at functions and we will implement something
like this.'''

# prepare dictionnary 
student = {
    'name' : '',
    'modules' : []
}

#ask user to enter their name
name = input('Hello student! Please enter your name: ')

def grades():

    #add name to the dictionary 
    student['name'] = name 

    #ask the student to enter the module name and repreat the question until the answer is null
    module = input('Enter module name: ')
    while  module != '':
        #append the module name in the list 
        student['modules'].append({'course_name' : module})
        #ask to enter another course name 
        module = input('Enter module name: ')
    
    #ask student to enter the grades for each course she  entered 
    for module in student['modules']:
        grade = input('Please enter your grade for {}: '.format(module['course_name']))
        module['grade'] = grade
       
    #print: student name 
    print(f"Student\t: {student['name']}")
        #print: course name: grade
    for module in student['modules']: 
        print("{}\t: {}".format(module['course_name'],module['grade']))


while name != '':
    grades()
    name = input('Hello student! Please enter your name: ')



