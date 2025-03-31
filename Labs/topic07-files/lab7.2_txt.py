# wekek 07, lab 1
# irene celebrin 
# read and write text files 

'''
task: 
Write a program that counts how many times it was run.
For this exercise will have to store data outside of memory, and that is accessible
each time the program is run, (persistent data). We would normally use a
database for something like this, but we can use a file.
To make life easier let’s assume that the file already exists. So, we can just read
the current count from it then overwrite it with the new count.
Create a file called count.txt and put in 0 into it
'''

'''
# the file count.txt already exists 

# create variable for counter 
counter = 'count.txt'

#read current counter and turn string into a number 
with open(counter, 'r') as f:
    count = f.read()

new_count = int(count) + 1
print(new_count)

with open(counter,'w') as f:    
    f.write(str(new_count))
'''
#import os to check if file exists
import os 

#import file 
FILENAME = "count.txt"



#create function to read in the number and transform from string to int 
def readNumber():
    try: 
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0
    
#test function 
#num = readNumber()
#print (num)

#create function write in a number and transform from int to str
def writeNumber(number):
    with open(FILENAME, 'wt') as f:
        f.write(str(number))


#main
if not os.path.isfile(FILENAME):
    print('file does not exist')
    writeNumber(0)

num = readNumber()
num += 1
writeNumber(num)
print(f'we have run this program {num} times')
