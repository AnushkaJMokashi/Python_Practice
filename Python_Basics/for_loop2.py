## to iterate over sequence of iterable objects
## nothing but iterating over strings,lists,tuples sets and dictionaries

print('== String ==')

name = 'Anushka'
for i in name:
    if(i == 's'):
        print("Something special")
    print(i)
    
print()
print("== List ==")

##--------------------------------------------------------
colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

##----------------------------------------------------
print()
print("== Range ==")

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(1,10,2): ## step function
    print(i)

##-----------------------------------------------------

