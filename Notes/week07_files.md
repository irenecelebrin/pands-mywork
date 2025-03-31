# week 07
### author: irene celebrin 

# FILES 

## video 0 - overview 

different types of files. 
explain resource in the section ?further watching/reading. have a look!!

## video 2 - Files 

reading and writing with files
txt, csv, json 

OPEN A FILE 

with open('workfile','r') as f: 
    read_data = f.read()

old way f = open('workfile','wb+')
f.write 
f.close 

this way is not the best because in case of error the file is not closed 

FUNCTIONS 
read()
readline()
write(data)
seek(offset)

MODES

r = assumes the file already exists 
r+ = opens existing file to write 
a = open existing file for appending to the end
w = opens a file and blanks out what is already there -- overwrites  
x = creates a new file, throws error if the file already exist s

t = text mode - automatically add new line at the end of each write. if you don't want tht you can but the keyword argumnt n (newline) 
b = binary mode 

resources 
w3 school 
official python documentation 


see code example

careful when you use w+ mode, you might need to use seek to put the pointer back to the beginning of the code 

remember that you need to specify separators / end of line 

### OS MODULE 

to check if a file/directory exists 
remove a file 
create a directory 

see jupiter notebook module 
see messingwithos.py

import os in the code 
you import the file 
then you add the code using the us function 

if os.path.exists(filename): 
    with open(filename, 'r) as f: 
    ....

## video 2 - File formats 

file formats 
module json
module csv  
xml
module pandas

binary files 
module pickle for storing and loading objects as binary files 


**json** check resources in the references section of the jupiter notebook and in the VLE 
json is javascript objetc natation 
it's the formst of the dictionary we created in the lab for week 6 

the module json has 2 objects dump() to create json files and load() to load existing json file to manipulate on pythin 

you can read the json file and store the data in a dict 

**csv files**
import csv 

you can read files with values seprataed by comma or any other delimiter 
see in jupiter notebook for reading and writing with csv files 



