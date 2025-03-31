# week 08, lab 1 
# irene celebrin 

# task Modify the program so that the “random” salaries are the same each time the
# program is run, to make the program easier to test, ie “seed” the random number generator. 

# import numpy module 
import numpy as np

# setting my requirements (min, max, desidered amount of numbers)
min_salaies = 20000
max_salaries = 80000
number_of_salaries = 10

# use seed function to tell the program I want the program to generate the same list of random numbers 
np.random.seed(1)
# generate random numbers with numpy (minimum number, max number, numer of numbers to generate)
salaries = np.random.randint(min_salaies, max_salaries, number_of_salaries)

print(salaries)
