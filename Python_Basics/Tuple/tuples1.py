## Manipulating Tuples

countries = ("Spain","Italy","India","England","Germany")
temp = list(countries)

## append item
temp.append("Russia")

## remove item
temp.pop(3) 
print(temp) 

## change item
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

## Concatenate
aplhabets = ('a','b','c')
concatenated_tuple = countries + aplhabets
print(concatenated_tuple)

## Occurrences of element
tup1 = (0,1,1,3,1,1,2,3,4,5,6,7)
res = tup1.count(1)
print("Count of 1 is: ",res)

## index
ind = tup1.index(1)
print("Index of 1 is: ",ind)

ind1 = tup1.index(3,4,8)
print(ind1) ## index of 3 from 4th to 7th index i.e. 7

## length of tuple
len = len(tup1)


