# week 08 

import numpy as np 

# int and string 
list_of_numbers = [1,2,3,5,'ciao']

print(list_of_numbers)

#int are turned into floats if you add a float
number = np.array([1,2,3,4, 3.5])
# int and string all all turned into strings 
number_2 = np.array([1,2,3,4,'ciaa']) 

print(type(number_2[0]))

rando = np.random.randint(100,200,30)

print(rando)