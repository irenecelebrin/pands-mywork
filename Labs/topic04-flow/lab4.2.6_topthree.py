# week 4, lab 2 
# author : irene celebrin

# task: Write a program (topthree.py) generates 10 random numbers (0-100) ,
# prints them out then prints out the top three. (there are concepts I have not
# covered yet in this question)

import random 

# create list with empty random numbers 
random_numbers = []

'''
# generate a random number until the length of the list is 10 
while len(random_numbers) < 10:
     random_number = random.randint(0,100)
     random_numbers.append(random_number)

# print each number in the list on a separate row      
for random_number in random_numbers: 
     print(random_number)
     random_number += 1
'''
#create for loop to create a random number between 0 and 100 for the range 1 to 10, and print list
for i in range(0,10):
    random_numbers.append(random.randint(0,100))
print(f'10 random numbers\t {random_numbers}')

#sort list in descending order
sorted_random_numbers = sorted(random_numbers, reverse=True)

# print only the first 3 elements of the sorted list 
top_three = []
count = 0 
while count < 3: 
    top_three.append(sorted_random_numbers[count])
    count += 1
print(f'The top 3 are\t\t {top_three}')
