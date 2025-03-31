# week 08, lab 1
# irene celebrin 

# task: Modify the program to make bar chart of the counties


import numpy as np
import matplotlib.pyplot as plt

# list of counties 
counties = ['Dublin', 'Wicklown', 'Kerry', 'Sligo', 'Derry']

county_numbers = [75, 22, 37, 11, 17]

plt.bar(counties, county_numbers)


plt.show()