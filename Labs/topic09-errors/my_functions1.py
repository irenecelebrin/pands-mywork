# week 09, raising errors
# irene celebrin 

import logging

# set logging to debug level (not really sure why)
logging.basicConfig(level=logging.DEBUG)

# define function. if the number is 0, empty list is returned, if less than 0, value error is raised 
def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be >0')
    a = 0
    b = 1
    fibonacci_sequence = [0]
    for i in range(1,number):
        fibonacci_sequence.append(b)
        a,b = b, a + b

    return fibonacci_sequence


# add in the main the assertion to check the code is working
# it will check that the behaviour is as expected for some functions
# it will also pass the error thrown if the number is <1. if no error is raised, it will raise a error
if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return for 0'
    assert fibonacci(1) == [0], 'incorrect return for 1'
    try:
        fibonacci(-1)
    except ValueError:
        pass 
    else:
        assert False, 'fibonacci missing ValueError'
    print('all good')