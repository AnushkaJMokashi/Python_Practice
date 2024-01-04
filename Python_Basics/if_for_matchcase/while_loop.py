## while is sometimes convinient than for loops if we just want to work over base condition
## used with complex conditions than numeric ones
## we can use else with while loop
i =0
while(i<=3):
    print(i)
    i = i +1

print("Done with while loop")\
    
x = int(input("Enter no. "))
while(i<= 20):
    i = int(input("Enter no. : "))
    print(i)
    
## Decrementing while loop
count = 0
while(count > 0):
    print(count)
    count -= 1
else:
    print("I am inside else")


## do while loop
## it will run irrespective of condition true or false

## emulate in python 
list1 = ["geeksforgeeks", "C++", 
         "Java", "Python", "C", "MachineLearning"]
while(True): 
    print(list1[i]) 
    i = i+1
    if(i < size and len(list1[i]) < 10): 
        continue
    else: 
        break