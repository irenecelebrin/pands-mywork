# week 06 
## author: irene celebrin 
## Functions 

### video 1 

**Built-in functions**

function + brackts and arguments, one or more separated by comma
some of the arguments can be named: print(1,2,3, sep='--')
examples: math, print, 

A function is an reusable bit of code, that can be used again and again, with different arguments 

**Using a function**

When you use a function, you don't care how it does the job, just that you are giving the right information it needs to work (the arguments)
Whn you write a function, you need to think about what you need and what you want to accomplish --> break in the function in smaller tasks 

- define a function:    def name_of_function(arg1,arg2):
                            #statements
                            return value
                        
                        x = lambda arg : arg *2 


-  call a function:     print('hi, 2, [])
                        
                        x=99

**Question** why printing with .format is not good????

You always need to define the function and then execute it, otherwhise nothing happens. 

**Arguments** you can add default arguments when defining a function and that means that if you don't input that argument, the default value will be used. 

Example 

def cube(number, power = 3)
    print(number)
    return (number ** power)

 
number = 3
power = 2
print(f'{number} at the power of {power} is cube(number, power))

### video 2

**Interface of a function**

A function is a blackbox 
In python named arguments (flags with an equal sign) can be added in any order. 
Example 

print(1,2,3, sep='', end='\t')
print('hi')

Sometimes arguments can be 'unnamed args'. you use *args ad arugemtn and you can use anything as arguemnt. 

*args  = argumetns 
**kwargs = keyword arguments 
*values 

### video 3 
*** Functions tutorial ***

how to re-use code again and again and again 

see code 

T2.1-readingnumbers.py

### video 4 

**variable scope**
Sometimes variable numbers are defined inside the function, and in that case you cannot change them from outside. Rember to use different names for variables that are passed as argumetns and variavle defined inside the code. 

L3.1scope.py

### video 5 
**lambda functions**

lambda function = anonymous functions 

code in L4.1lambda functions.py

why using lambda functions? useful when passing a function inside another function, also it will make the function more flexible. 
You can also use lambda functions to sort dictionnaries 
You cart sort listis very easily with the built-in sort() function, but not dictionnaries. 

### video 6 
**modules**

As for built-in functions, there are built-in modules (for example print())
These don't need to be imported, in other cases you need to import or install the module to be able to use those functions (for example math, daytime...)

python modules in w3school 

code example in L4.5-messing.withModules.py

***How to use functions inside modules***

1) import module_name 

var = module_name.function

2) import module_name as shortened_name

var = shortened_name.function()

3) from module_name import function_name 

var = function_name()

For example, you can import from github the Github function to make commits automatically to your repo (check docu)
If you import a module that doesn't exist or work, you might need to install it with:    pip install



***Create your own modules***

If you want to create a big program you can create different parts of code and store them in different files with different functions and then import them into the main file 
Also useful if you want to create a config file to store API keys or info that you don't want to display and make public

check how the program looks like in only one file in T2.2lab-original.py and using modules in T2.2

Configuration files: example in config.py. in this case, you can push the code to gitHub but not the config, so your data will not be shared. 

remember that to import your modules they have to be in the same directory (folder) as the current file, otherwhsie you hvae to use anothe ways to import them. 



