# week 03, lab 2 
# author: icelebrin 

##Write a program (floor.py), that takes in a float and outputs an int rounded down, you will need the math module math.floor()
import math 


number_to_floor = float(input('Enter a float number: '))
floored_number = math.floor(number_to_floor)


print('{} floored is {}'.format(number_to_floor,floored_number))
