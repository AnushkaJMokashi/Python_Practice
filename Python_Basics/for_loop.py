exp = [2340, 2500, 2100,3100, 2980 ]

# total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
# print(total)

"-----------------"
total = 0
for item in exp:
    total = total + item
print(total)

"----------------------"

for i in range(10):
    print(i)
print("--------------------------")

for i in range(1,11):
    print(i)
    
print("--------------------------")
print("== list ==")
for i in range(len(exp)):
    print('Month: ', (i+1), "  Expense: ",exp[i])
    total = total + exp[i]
print("total", total)


print("--------------------------")

key_loc = "chair"
locations = ["garage", "room", "chair", "closet"]
for i in locations:
    if i==key_loc:
        print("Key is found in : ",i)
        break
    else:
        print("Not found in : ",i)

print("--------------------------")

