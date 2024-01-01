
## without comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []

for var in input_list:
	if var % 2 == 0:
		output_list.append(var)

print("Output List using for loop:", output_list)

print()
print('--------------------------------------------------------------')

## List Comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
							list_using_comp)

print()
print('--------------------------------------------------------------')
