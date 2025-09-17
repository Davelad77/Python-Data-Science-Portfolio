# ask the user to enter the name of their favourite restaurant
# ask the user to enter their favourite number and use casting to store as an integer
# print both variables
# once this works try casting the restaurant name as an integer - what happens? add comments to explain why

restaurant = input("What is your favourite restaurant? ")
number = int(input("What is your favourite number? "))
print(restaurant)
print(number)
print(int(restaurant)) # This will give an error because the restaurant name is a string and cannot be converted to an integer.