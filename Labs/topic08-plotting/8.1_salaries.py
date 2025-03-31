# week 08, lab 1 
# author irene celebrin 

# Write a program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000).

# import numpy module 
import numpy as np

min_salaies = 20000
max_salaries = 80000
number_of_salaries = 10

# generate random numbers with numpy (minimum number, max number, numer of numbers to generate)
salaries = np.random.randint(min_salaies, max_salaries, number_of_salaries)

print(salaries)

