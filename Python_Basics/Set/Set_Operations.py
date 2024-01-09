def accept_set(A,str):
	n = int(input("Enter the no. of students who play %s : "%str))
	for i in range(n):
		x = input("Enter the name of student %d who play %s : "%((i+1),str))
		A.append(x)
	print("Set Accepted successfully !!")


def display_set(A,str):
	n = len(A)
	if(n==0) :
		print("\n Group of students who play %s : {}"%str)
	else : 
		print("\n Group of students who play %s : {"%str,end='')
		for i in range (n-1) :
			print("%s ,"%A[i],end='')
		print("%s}"%A[n-1])

def search_set(A,X) :
	n = len(A)
	for i in range(n):
		if(A[i]== X):
			return (1)
		return (0)

def find_intersection_set(A,B,C):
	for i in range(len(A)):
		flag = search_set(B,A[i])
		if(flag == 1):
			C.append(A[i])


def find_difference_set(A,B,C):
	for i in range(len(A)):
		flag = search_set(B,A[i])
		if(flag == 0):
			C.append(A[i])

def find_union_set(A,B,C):
	for i in range(len(A)):
		C.append(A[i])
	for i in range (len(B)):
		flag = search_set(A,B[i])
		if(flag == 0):
			C.append(B[i])

def main() :
	Group_A = [];
	Group_B = [];
	Group_C = [];


	while True :
		print("\n\t1 : Accept the information.  ")
		print("\n\t2 : List of students who play both Cricket and Badminton.  ")
		print("\n\t3 : List of students who play either Cricket or Badminton but not both.  ")
		print("\n\t4 : Number of students who play neither Cricket nor Badminton.  ")
		print("\n\t5 : Number of students who play Cricket and Football but not Badminton. ")
		print("\n\t6 : Exit")
		ch = int(input("Enter Your Choice : "))
		Group_R = []

		if(ch == 6):
			print("End of Program ")
			break
		elif(ch == 1):
			accept_set(Group_A,"Cricket")
			accept_set(Group_B,"Badminton")
			accept_set(Group_C,"Football")
			display_set(Group_A,"Cricket")
			display_set(Group_B,"Badminton")
			display_set(Group_C,"Football")
		elif(ch==2):
			display_set(Group_A,"Cricket")
			display_set(Group_B,"Badminton")
			find_intersection_set(Group_A,Group_B,Group_R)
			display_set(Group_R,"Play both Cricket and Badminton")
		elif(ch == 3):
			display_set(Group_A,"Cricket")
			display_set(Group_B,"Badminton")
			R1 = []
			find_union_set(Group_A,Group_B,R1)
			R2 = []
			find_intersection_set(Group_A,Group_B,R2)
			find_difference_set(R1,R2,Group_R)
			display_set(Group_R,"either Cricket or Badminton but not both ")

		elif(ch == 4):
			display_set(Group_A,"Cricket")
			display_set(Group_B,"Badminton")
			display_set(Group_C,"Football")
			R1 = []
			find_union_set(Group_A,Group_B,R1)
			find_difference_set(Group_C,R1,Group_R)
			display_set(Group_R,"neither Cricket nor Badminton ")
			print("Number of students who play neither cricket nor Badminton = %s "%len(Group_R))

		elif(ch == 5):
			display_set(Group_A,"Cricket")
			display_set(Group_B,"Badminton")
			display_set(Group_C,"Football")
			R1 = []
			find_intersection_set(Group_A,Group_C,R1)
			find_difference_set(R1,Group_B,Group_R)
			display_set(Group_R,"Cricket and Football but not Badminton")
			print("Number of students who play Cricket and Football but not Badminton = %s"%len(Group_R))
		else:
				print("Invalid Choice")

main()
quit()



