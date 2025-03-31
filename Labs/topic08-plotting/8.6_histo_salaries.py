# week 08, lab 1 
# irene celebrin 

# task: Write a program that plots a histogram of the salaries (from Question 1)

# import numpy and matplotlib  
import numpy as np
import matplotlib.pyplot as plt 

min_salaies = 20000
max_salaries = 80000
number_of_salaries = 10

# generate random numbers with numpy (minimum number, max number, numer of numbers to generate)
salaries = np.random.randint(min_salaies, max_salaries, number_of_salaries)

# create historigram 
plt.hist(salaries, label = 'salaries')
# add legend
plt.legend()
plt.show()

