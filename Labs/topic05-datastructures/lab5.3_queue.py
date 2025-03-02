# week 05, lab 1 
# author: icelebrin 
# list and for loops 

# task Create a program that puts 10 random numbers into a queue(list), the
#program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

import random 
#create a queue list 
queue = []
queue_len = 10

# for loop to generate 10 random numbers and add them to the list. 
for i in range (0,queue_len):
    queue.append(random.randint(1,100))

# now the queue list includes 10 numbers waiting 
print(f'Queue is {queue}')


# for loop to examine a number a print the rest of the queue 
for i in range(len(queue)):
    current_number = queue[i]
    print(f'Current Number is {current_number} and the queue is:\t{queue[i+1:]}') 

print('The queue is now empty')

#alternative method 
'''

while len(queue) != 0:
    current_number = queue.pop(0)
    print (f"current Number is {current_number} and the queue is {queue} ")
pri}nt ("the queue is now empty")

'''
