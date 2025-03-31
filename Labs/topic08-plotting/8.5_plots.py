# week 08, lab 1 
# irene celebrin 

# task: Write a program that plots the function y = x2

# import modules 
import numpy as np 
import matplotlib.pyplot as plt

# define x points 
x = np.array(range(1,100))
y = x ** 2 

plt.plot(x,y)
plt.show()