# week 03 lab 02
# author: icelebrin 

'''
Write a program (normalise.py) that reads in a string and strips any leading
or trailing spaces, the program should also convert the string to lower case.
The program should also output the length of the input and output strings.
See Python - String Methods (w3schools.com) for more information of string
methods.
'''

#input string
input_string = input('Enter a string: ')

#strip white spaces and reduce to lower case 
normalised_string = input_string.strip().lower()
input_length = len(input_string)
output_length = len(normalised_string)


print('That string normalised is: \'{}\''.format(normalised_string))
print('We reduce the input string from {} to {} characters.'.format(input_length,output_length))



