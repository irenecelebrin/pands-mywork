# week 08, lab 1
# irene celebrin 

# task Write program that has a list of counties, make it a long list (pick from five
# counties). Make some counties appear more than others. Make a pie chart of the counties.

import numpy as np
import matplotlib.pyplot as plt

# list of counties - labels 
counties = ['Dublin', 'Wicklown', 'Kerry', 'Sligo', 'Derry']

# numbers - amounts 
county_numbers = [75, 22, 37, 11, 17]

# create pie chart 
plt.pie(county_numbers, labels = counties)

# show chart 
plt.show()

