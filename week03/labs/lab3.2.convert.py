# week 03 lab 2 
# author: icelebrin 

'''
I am writing an application, at the moment, in it I take an input of an amount
in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a
minus sign, and the bank takes in the amount in cent, (944). Write a program
called convert.py that takes in a float amount of dollars and returns that
absolute amount in cent.

'''

number_to_convert = float(input('Enter an amount: '))

number_converted = int(abs(number_to_convert * 100))

print (f'That amount is cent is: {number_converted}')
