def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  #this body can be written later

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)


## Pass
# When the user does not know what code to write, So user simply places a pass at that line. 
# Sometimes, the pass is used when the user doesn’t want any code to execute. So users can simply place a pass where empty code is not allowed, 
# like in loops, function definitions, class definitions, or in if statements. So using a pass statement user avoids this error.

## Why Python Needs “pass” Statement?
# If we do not use pass or simply enter a comment or a blank here, we will receive an IndentationError error message.