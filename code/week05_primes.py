# week 05 


# create a program to check which numbers between 0 and 100 are prime numbers -- they are prime numbers if they cannot be divided by any number and give an integer 

# create empty list to store prime numbers
primes = []
up_to = 101 #mit's better to store  value in variables so it's easier to dientify and change them in multiple occurrences

for candidate in range(2,up_to): #you want to use 101 otherwhise the loop will stop at 99. 
    isPrime = True
    for divisor in range(2, candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break  # this will break the loop and restart with the next candidate  
    if isPrime:
            primes.append(candidate)
    
print(primes)