# week 07, lab 1
## author icelebrin 

# quiz  

with open("test-b.txt", "w") as f:
 data = f.write("test b\n") # returns the number of chars written
 print (data)

with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)
 