
x = int(input("Enter no. : "))
match x:
    case 0:
        print("Zero")
    case _ if x != 90:
        print("not 90")
    case _ if x!= 80:
        print("not 80")
    case _:
        print(x,"default" ) #default case
        
## no need of break statement like c,c++
## still similar to switch case of c++
