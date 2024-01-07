## Tuples : 

# Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuples are immutable

tup = (1)
print(type(tup),tup)
tup1 = (1,)
print(tup1)

# tup1[0] = 90  
print(tup1)

# access the elements 
tup2 = (1,2,76,342,32,"green",True)
print(type(tup2),tup2)
print(tup2[0])
print(tup2[-1])
print(tup2[2])

if 342 in tup2:
    print("Yes")
else:
    print("No")
    
tup3 = tup2[1:4]