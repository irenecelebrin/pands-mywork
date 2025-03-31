# week 08, lab 1 
# irene celebrin 

# task .Add a line to this plot that shows y= x2 in a different colour

# import numpy and matplotlib  
import numpy as np
import matplotlib.pyplot as plt 

# data for salaries and age 
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
plt.scatter(ages, salaries)
plt.title('random plot')
plt.xlabel('ages')
plt.ylabel('salaries')

# data for x and y 
x = np.array(range(1,100))
y = x ** 2

# create plot 
plt.plot(x,y, color = 'green', label = 'y = x**2')
plt.legend()


# show 
plt.show()



