# ask the user to enter 3 different integers
# print out:
# the sum of the numbers
# the first number minus the second number
# the third number multiplied by the first number
# the sum of the numbers divided by the third number

int1 = int(input("Please enter the first integer: "))
int2 = int(input("Please enter the second integer: "))
int3 = int(input("Please enter the third integer: "))
sum = int1 + int2 + int3
diff = int1 - int2
multiple = int3 * int1
division = sum / int3
print("The sum of the numbers is: ", sum)
print("The first number minus the second number is: ", diff)
print("The third number multiplied by the first number is: ", multiple)
print("The sum of the numbers divided by the third number is: ", division)
