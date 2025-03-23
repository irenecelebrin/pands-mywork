
#week 07# reading and writitng files 


filename = "data.txt"


with open(filename, 'rt') as f:
    # read the whole file 
    '''data = f.read()
    print(data)'''
    # read each line separately --> one line between each line 
    '''for data in f:
        print(data)'''
    # remove the lines in the middle 
    for data in f: 
        # best way 
        print(data.strip())
        #print(data, end ='')
        #print(data[:-1])


#min this case you create the text with the write mode 
#with write everything is added together, you need to add your preferred separator 
with open('data2.txt','wt') as f:
    f.write('how now\n')
    f.write('brown cow')

with open('data2.txt','rt') as f:
    data2 = f.read()
    print(data2)

# or you can do both with w+
#mps remember to use seek to go back with the pointer to the beginning of the file 