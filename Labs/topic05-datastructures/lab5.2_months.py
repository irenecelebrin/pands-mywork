# week 05, lab 1
# author: icelebrin 
# tuples 

# task Create a tuple that stores the months of the year, from that tuple create
# another tuple with just the summer months (May, June, July), print out the 
# summer months one at a time

# create a tuple storing the months of the year

months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov', 'Dec')

summer = months[4:7]
for month in summer: 
    print(month)