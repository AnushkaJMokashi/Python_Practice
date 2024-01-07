l = [4,5,9,3,4,7]
print(l)
##Append
l.append(10)

##sort
l.sort()

## Reverse
l.reverse()
print(l)

## Index
l.index(7)  ## arg is the value to be searched ##returns index of occurence of element

## Count
l.count(4)

## m references to l hence value in l changed
m = l
m[0] = 0
print(l)

## value in m changed
m = l.copy()
print(l)
 
## Insert at particular index
l.insert(1,10)
print(l)

## Extend
m=[900,1000,1100]
l.extend(m)
print(l)
m.extend(l)
print(m)
 
## concat lists
k=l+m
print(k)