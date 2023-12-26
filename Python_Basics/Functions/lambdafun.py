# A function without name is called anonymus function.
# Defined by using the keyword as 'lambda'

#Example:

def square(x):  # square is name of function
    return x*x

a = square(5) # function call
print(a)

## Using Lambda Function

f = lambda x: x*x
val = f(5)
print(val)

## here no need to write the return 
## hence we can pass this function to another function
## makes easier for processing the data


## It can be used with filter(fun,seq)
lst = [10,20,30,45]
lst1 = list(filter(lambda x :(x%2 == 0), lst))
print(lst1)

    

##It can be used with map
lst = [10,20,30,45]
lst1 = list(map(lambda x : x*x, lst))
print(lst1)

lst = [10,20,30,45]
def squares(x):
    return x*x
lst1 = list(map(squares, lst))
print(lst1)

##With reduce
from functools import *
sum = reduce(lambda a,b:a+b,lst1)
print(sum)

