## breaks from the loop at the given condition
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
print('------------------------------------')
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break
print('------------------------------------')
## The continue statement skips the rest of the loop statements and causes the next iteration to occur.
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
print('------------------------------------')
for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
print('------------------------------------')
  
