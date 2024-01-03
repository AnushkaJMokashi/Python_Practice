# Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

## Enumerate



l1 = ["Hi", "Hello", "Bye"]
s1 = "geek"
 

obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
 

print (list(enumerate(s1, 2)))