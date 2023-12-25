x = None
y = 10
z = "Hello"

if x is y:
    print("x and y are equal")
elif x is z:
    print("x and z are equal")
else:
    print("x and y are not equal")

# output: x and y are not equal

if x is False:
    print("x and False are equal")
elif x is True:
    print("x and True are equal")
else:
    print("x and False are not equal")

# output: x and False are not equal

if x == 0:
    print("x and 0 are equal")
elif x == "Hello":
    print("x and Hello are equal")
else:
    print("x and 0 are not equal")

# output: x and 0 are not equal

