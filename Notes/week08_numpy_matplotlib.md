# week 08

## Looking ahead 
check assessment section on VLE for information on the project 

Anaconda has modules already installed, locally you need to install them (pip install modulename)
Modules: 

numpy --> packs data in more efficient ways (arrays) and makes the program faster 
matplotlib --> to make plots 
pandas --> data analytics on spredsheets/taular form

###  Video 1 - Numpy 
Efficient way of listing data. 
Numpy deals with arrays 


Numpy: 
- quick way to go through large datasets
- multidimensional arrays 
- built in functions for metrics manipulation -- matrix functions 
- indexing is different from list --> multidimension arrays 
- same licing 
- all elements in an array should be the same type --> numpy will tranform the elements to make it all the same type, or throw error message 
- reshaping 
- combining arrays together 
- random number generator -- generate random numbers, normalised data 

References: real python, w3school, numpy.org, github numpy ReadMe

Differences between numpy and lists 

- concatenations are different
- multiplications and divisions 
- data types 

***random numbers** are quite handy 

np.random.randInt for random integers 
np.random.normal to create numbers around a given mean, sd, average, size 
you can use np.seed(1) to have always the same random number(s) generated 

### vide 2 - Matplotlib 

2 ways of using it: objetc-orientated or non-object oriented non-obj oriented is better 
Based on matlab 
it makes plots 

plot vs graph 
Graph has nodes and links between the nodes 
plots is what in school is called a graph 

types of plots: 
-line plots
- scatter plots 
- histograms 
- pie charts 

see the anatomy of the plot: 
axes (x,y) with ticks (scales), the lune (plot) or dots (scatter plots)
labels for x and y axes
legend
markers for scatteplots 
grid 
title 

#### Using matplotlib 

- stateful see w3school 
- stateless (object oriented) 

Statless 

you can import and create the arrays for the axes, show the plot and then the program for visualization will open. 
you can add lables and change the aesthetics from the program or programmatically on the script 

see code examples in the code section 

### C born 
based on matplotlib, you can use for advanced plots for reports 
