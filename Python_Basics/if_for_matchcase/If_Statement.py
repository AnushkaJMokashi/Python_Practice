num = input("Enter a number : ")
num = int(num)

if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

"----------------------------------"

indian = ["samaosa", "dal", "naan"]
chinese = ["egg roll", "fried rolls"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name : ")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("Unknown...")
