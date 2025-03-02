# week 04, lab 1 
## author: irene celebrin 

'''task 
In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
equal to a Distinction.
How would you modify the program in 1 to deal with this?
'''


# ask percentage 
# grade -- change condition in the if statements to half numbers 
grade = float(input('Please enter a percentage: '))

'''
# grade --- change condition in the original if statement, modifying 69 with 69.5
# print grade with for loops and as many conditions as the available grades 
if grade < 0 or grade > 100:
    print('Please enter a percentage between 0 ans 100')
elif grade <= 39.5:
    print('Fail')
elif grade > 39.5 and grade<= 49.5: 
    print('Pass')
elif grade > 49.5 and grade <= 59.5:
    print('Merit 2')
elif grade > 59.5 and grade <= 69.5: 
    print('Merit 1')
else: 
    print('Distinction')
'''

# grade2 -- round input number with method #round()

#ask for percentage 
grade2 = input('Please enter a percentage: ')

#round mumber to float with 0 decimal numbers
rounded_grade = round(grade2,0)


#if statements 
if rounded_grade < 0 or rounded_grade > 100:
    print('Please enter a percentage between 0 ans 100')
elif rounded_grade < 40:
    print('Fail')
elif rounded_grade >= 40 and rounded_grade<= 49: 
    print('Pass')
elif rounded_grade >= 50 and rounded_grade <= 59:
    print('Merit 2')
elif rounded_grade >= 60 and grade2 <= 69:
    print('Merit 1')
else: 
    print('Distinction')
