# The first code explains that the set cannot have a duplicate value. Every item in it is a unique value. 
# The second code generates an error because we cannot assign or change a value once the set is created.
# We can only add or delete items in the set.


 
# a set cannot have duplicate values
myset = {"Geeks", "for", "Geeks"}
print(myset)
 
# values of a set cannot be changed
myset[1] = "Hello"
print(myset)


## --- unordered elements.. ----
# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
myset.add("d")
print(myset)

# Types
# set	Mutable unordered collection of distinct hashable objects.
# frozenset	Immutable collection of distinct hashable objects.
