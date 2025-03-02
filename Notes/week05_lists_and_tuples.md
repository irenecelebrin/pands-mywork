# week 05 


## video 1 
## Lists and Tuples 

**LISTS**
a list can store any types of values at the same time. Numbers, strings, even other lists. 
They are **ordered** and **mutable**. This means that you can identify elements based on where they are in the list (index) and access the list elements to change them.

len(list)

list.append()
list + for concatenation 
list.sort 
you can slide them 

see jupiter notebook for functons 


**DEBUGGER** little excursus ion debugger



**TPLES**
declared with round brackets or nothing. ypu cannot add or modify tuples 

t= (1,2,3)
t = 1,2,3
print(t)

x,y,z = t 
this mill mean that the tuple is (1,2,3)
very useful with functions and variables 


ts 
# video 2 
## Dictionaries 

defined inside graph brackes 
    x =  {'varl' : 'value1',}
access values with square brackets 
    x['varl] = newValue
    print(x['varl'])
value pariss, which is a pair of key and associated value. the associated value can be anything (list, number, string, tuple...). A dcitionary can even contain a dictionary 
you can use the get funxtion if not sure a key exists
    print[x.get[var1]] in this way, if you are not sure of the key value, you'll get None as answer if the key is not found, instead of an error message
you can use the update function to add/modify content

check more on W3schools 



