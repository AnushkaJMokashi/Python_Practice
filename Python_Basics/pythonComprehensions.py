# Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, sets, dictionaries, etc.) 
# using previously defined sequences. Python supports the following 4 types of comprehension:

# List Comprehensions
# Dictionary Comprehensions
# Set Comprehensions
# Generator Comprehensions

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

## Dictionary Comprehension
input_list = [1,2,3,4,5,6,7]
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)

print()
print('--------------------------------------------------------------')

## with zip function
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key:value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:", 
										dict_using_comp)

print()
print('--------------------------------------------------------------')

##set
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
							set_using_comp)
print()
print('--------------------------------------------------------------')

## Generator Comprehensions
# generator comprehensions use circular brackets whereas list comprehensions use square brackets.
# The major difference between them is that generators don’t allocate memory for the whole list.
# Instead, they generate each value one by one which is why they are memory efficient.
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')


print()
print('--------------------------------------------------------------')

## Combining multiple lists
a = [1, 2, 3]
b = [7, 8, 9]
c = [(x + y) for (x,y) in zip(a,b)]  # parallel iterators
# output => [8, 10, 12]
d = [(x,y) for x in a for y in b]    # nested iterators
# output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)] 

