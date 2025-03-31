# week 07, lab 1
# by irene celebrin 

# task Write a function that will store a simple Dict to a file as JSON. TEST IT

# import json module 
import json 

# my dict
student = {
    'name' : 'ivan',
    'subject' : [
        {'history' : 1},
        {'math' : 2},
        {'science' : 1}
    ]
}

def write_dict(obj):
    with open('dict.json','wt') as f:
        json.dump(obj, f) 

write_dict(student)

