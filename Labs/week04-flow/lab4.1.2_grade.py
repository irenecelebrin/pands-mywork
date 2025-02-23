# week 04, lab 1
## author: icelebrin 

'''task 
Write a program (grade.py) that reads in a student’s percentage mark and
prints out corresponding the grade (the program should check that the
percentage is valid:
• Under 40% => Fail
• Between 40% and 49% => Pass
• Between 50% and 59% => Merit 2
• Between 60% and 69% => Merit 1
• Over 70% 
'''

# ask percentage 

grade = float(input('Please enter a percentage: '))

# print grade with for loops and as many conditions as the available grades 
if grade < 0 or grade > 100:
    print('Please enter a percentage between 0 ans 100')
elif grade < 40:
    print('Fail')
elif grade >= 40 and grade<= 49: 
    print('Pass')
elif grade >= 50 and grade <= 59:
    print('Merit 2')
elif grade >= 60 and grade <= 69: 
    print('Merit 1')
else: 
    print('Distinction')

