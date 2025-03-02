# week 05, lab 1 
# author: icelebrin  

'''
Write a program that will read in the data for the data structure above, ie
reads in a student’s name, then keeps reading in their modules and grades
(until the user enters a blank module name),
You can break this up into two parts:
a. Just read in the module names until the user enters blank,
b. Then read in the grade as well
This program can just read in one student (and their module details).

'''



#framework
'''
student = {
    'name' : 'Mary',
    'modules' : [
        {
            'course_name' : 'Programming',
            'grade' : 45
        },
        {
            'course_name' : 'History',
            'grade' : 99
        }
    ]   
}

'''

# prepare dictionnary 
student = {
    'name' : '',
    'modules' : []
}

#ask user to enter their name
name = input('Hello student! Please enter your name: ')

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


