# Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. 
# They are represented the @decorator_name in Python and are called in a bottom-up fashion. For example:

# returns a function from a function

# decorator function to convert to lowercase
def uppercase_decorator(function):
   def wrapper1():
       func = function()
       string_lowercase = func.upper()
       return string_lowercase
   return wrapper1



# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper

def hello1():
   return 'Hello World'
print(hello1()) 

## these decors are applied to all next functions
@splitter_decorator # this is executed next
@uppercase_decorator # this is executed first


def hello2():
   return 'Hello World'
print(hello2())   # output => [ 'hello' , 'world' ]
