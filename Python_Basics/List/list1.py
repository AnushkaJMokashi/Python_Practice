l = [3,5,6]
print(l)
print(type(l))
## list are ordered collection of data items
print(l[0])
## negative index are allowed
print(l[-3]) 
## pos index = len-3
print(l[5-3])
print(l[len(l)-3])

print('-------------------------------------')
## Any datatype can be there
l = [1,"A",8.9,True]
print(l)

print('-------------------------------------')
if 7 in l:
    print("yes")
else:
    print("No")
    