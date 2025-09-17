# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"           # SYNTAX ERROR - need to surround text with "" to define a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"     # SYNTAX ERROR - in order to concatenate different variable types you must use f-string. 
                                                                                                # LOGIC ERROR - number_of_teeth and animal_type are switched so the sentence would be nonsense

print(full_spec)     # SYNTAX ERROR - print variable must be contained in brackets
