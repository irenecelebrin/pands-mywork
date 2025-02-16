# week 03 lab 1 
# author: irene celebrin


# 1.  Why does this expression cause an error? How can you fix it? 
'''
message = 'I have eaten ' + 99 + ' burritos.'
print (message)
'''

## answer 
## Because 99 should be inside the string of the answer. you can correct it formatting it into the strinf

burritos_n = 99
message = f'I have eaten {burritos_n} burritos.'
print (message)

## another solution: 

burritos_n = 99
message = 'I have eaten {} burritos.'.format(burritos_n)
print (message)

# 2. Why is eggs a valid variable name while 100 is invalid?

## Because variables need to include letters. you can't use numbers to name variables

# What three functions can be used to get the integer, floating-point number, or string version of a value?
## You can use int(), float(), str()

