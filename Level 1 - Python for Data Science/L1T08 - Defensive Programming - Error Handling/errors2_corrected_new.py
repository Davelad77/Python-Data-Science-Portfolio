# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"     # RUNTIME ERROR - as a string Lion needs to be enclosed in "
animal_type = "cub"
number_of_teeth = 16

print(f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")

# print(full_spec)        # SYNTAX ERROR - missing parentheses

# LOGIC ERROR - defining sull_spec as a string then printing that string does not include the contents of the variables
# RUNTIME ERROR - you must use an f-string to include variable contents in a string output
# LOGIC ERROR - the output refences the variables in the incorrect order
