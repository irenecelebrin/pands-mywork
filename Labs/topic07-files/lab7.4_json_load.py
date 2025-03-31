# week 07 
# by irene celebrin 
# json load 

# task: Write a function that will read in a dict object from file. TEST IT

import json

# create function to load dictionary from json file 
def read_dict(): 
    with open('dict.json') as f:
        return json.load(f)


# store the dict in a variable 
student = read_dict()
# print dict in the console 
print(student)
