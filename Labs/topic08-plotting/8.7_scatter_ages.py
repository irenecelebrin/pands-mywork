# week 08, lab 1 
# irene celebrin 

# task . Write a program that makes a list called ages that has, the same number random values as salaries, (range:21 to 65) . Make scatter plot of this data

# import numpy and matplotlib  
import numpy as np
import matplotlib.pyplot as plt 

min_salaries = 20000
max_salaries = 80000
number_of_salaries = 100

min_age = 21
max_age = 65

# generate random numbers with numpy (minimum number, max number, numer of numbers to generate)
salaries = np.random.randint(min_salaries, max_salaries, number_of_salaries)
# generate 10 random numbers for ages 
ages = np.random.randint(min_age, max_age, number_of_salaries)

# create historigram
plt.scatter(salaries, ages)
# add legend
plt.legend()
plt.show()

