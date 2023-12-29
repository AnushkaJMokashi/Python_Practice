def print_pairs(arr, N):
   # hash set
   hash_set = set()
    
   for i in range(0, len(arr)):
       val = N-arr[i]
       print(val)
       if (val in hash_set):    #check if N-x is there in set, print the pair
           print("Pairs " + str(arr[i]) + ", " + str(val))
       hash_set.add(arr[i])

# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 3
print_pairs(arr, N)



def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
print(add_nums(2, 10))