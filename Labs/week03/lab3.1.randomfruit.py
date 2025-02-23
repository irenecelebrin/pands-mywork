# week 03 lab 1 
# author : irene celebrin 

# Write a program (randomfruit.py) that prints out a random fruit.
'''
import random 

fruit_list = ['strawberry', 'blueberry', 'respberry', 'blackberry', 'cranberry']

print(f'A random fruit: {random.choice(fruit_list)}')

'''
# Another way 
'''
import random 

fruit_list = ['strawberry', 'blueberry', 'respberry', 'blackberry', 'cranberry']

fruit_index = random.randint(0,len(fruit_list)-1)

random_fruit = fruit_list[fruit_index]

print('A random priece of fruit: {}'.format(random_fruit))

'''

### Modify the program in 6 (randomFruit2.py) so that it uses a tuple ( ) not a list [ ]

import random 

fruit_tuple = ('strawberry', 'blueberry', 'respberry', 'blackberry', 'cranberry', '7', True, '33.5')

fruit_index = random.randint(0,len(fruit_tuple)-1)

random_fruit = fruit_tuple[fruit_index]

print('A random priece of fruit: {}'.format(random_fruit))