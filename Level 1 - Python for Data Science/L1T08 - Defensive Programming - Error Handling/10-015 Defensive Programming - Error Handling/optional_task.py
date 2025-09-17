# Borrowed this program from an earlier task to use as a base to add errors
#
# The user inputs a number.
# The program then outputs all the EVEN numbers from 0 to that number, using a for loop and if statement.

print "*Printing even numbers in a range*"  # this will produce a compilation/syntax error for missing parenthese
range_num = int(Input("Enter the upper bound of the range (max number you'd like to go up to): \n"))  # this will produce another syntax error for capitalising input


for i in range (0, rangenum):   #  this will produce out runtime error as rangenum is not defined
	if i % 2 != 0: # this will produce the logical error as by calculating i not equal to zero it will output odd numbers
		print(i)