# week 08: Errors - toggle
### irene celebrin 

## Video 1: Exception and errors

bugs: 
- syntax errors
- runtime exceptions 
they get thrown by python, for example if you try to open a file the does not exist 
- semantic errors
the hardest to find, when something in the logic is not working so the program gets stuck 

**Runtime errors** 
or rurntime exceptions (java) 
- file not found
- divide by 0
- list index out of bouns 
- attribute not found 

philisophy: try to guess where in your code things can go wrong, and print messages in those parts 
so you can use Try... Except

check the real python tutorial on exceptions 

**Throw exceptions**
code: messing with exceptions.py
In this case the error message is thrown, but it's not easy to read for a user. so you want to try to catch it and add a easy answer for the user. 
you also want to catch that particular error, otherwhise the message will be shown for any error. 
Hence, you use the names of th errors and throw different messages according to the type of errors you get 

except IndexError as ie 

**Raise exceptions**
code: raiseAnException.py 

raise ValueError('message')
or you can define a **custom exception** creating a class to define it. 
check jupiter notebook 


Only catch exceptions if you plan to do somethingg with it. 
Do not catch an exception and just pass it 
if you are the only person running the project, catching expcetions is useful. Otherwise you can just debug yourself 
Exception catching is powerful when used with logging 

## Video 2: Test cases 

code that checks that your code is doing what you are expecting 

assert keyword is used to make sure something is a given value 

you can write test cases in different file or in the same module file that combines different modules 

Tututorial Getting started with testing in the real python 
it includes unit testing 

You can test the code in a separate python file
Testmyfunctions.py
- manually testing your code 

Automatic testing 
- unit tests 
- put the test functions in name = main. Or you can test it in the main module. However, you need to use the name function for that 

if __name__ == "__main__"


Why testing your code? 
- so you know your function is working 
- it gives sample code using your function 
- if your code is using other code, and that code is change, it gives reassurance that your code will still work 
- DevOps. 

## video 3 - logging 

logging has different levels, so you can set levels for debugging or higher levels. 
it is more flexible than print statements 

different levels: debug, info, warning, error, critical. So that you see those messaging only when you are working at those levels 

check out real python tutorial on logging, python documentation 

showLogging.py 

import logging first 

check different levels
you can change the basic config too 

- logging.basicConfig(level=logging.WARN) in this way you print in the console

- logging.basicConfig(filename = ./mainlog.log,
                    level=logging.WARN) 

in this was you print in the file you specified 
every time you run the code, the messages are printed in the log file 

