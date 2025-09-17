# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")   # SYNTAX ERROR - missing parentheses around text
print("\n")                             # SYNTAX ERRORS - unnecessary indent and missing parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"              # SYNTAX ERRORS - unnecessary indent and incorrect operator, should just be =
age = int(age_Str[0:2])               # SYNTAX ERROR - unnecessary indent, have to use some kind of indexing to remove the text so the variable can be cast as an integer
print(f"I'm {age} years old")         # SYNTAX ERROR - unnecessary indent and RUNTIME ERROR - should use age with f-string as can't concatenate an int in a string

# Variables declaring additional years and printing the total years of age
years_from_now = 3                      # SYNTAX ERROR - unnecessary indent and integer defined as string (remove the inverted commas)
total_years = age + years_from_now      # SYNTAX ERROR - unnecessary indent and RUNTIME ERROR - trying to sum a string with an integer

print(f"The total number of years: {total_years}")     # SYNTAX ERROR - missing parentheses, RUNTIME ERROR - answer_years is undefined (should be total_years) and use f-string to concatenate different variable types

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6       # RUNTIME ERROR - total is not defined, should be total_years and LOGIC ERROR - haven't added the extra 6 months detaile din the print statement below
print(f"In 3 years and 6 months, I'll be {total_months} months old")       # SYNTAX ERROR - missing parentheses and RUNTIME ERROR - use f-string to concatenate different variable types

#HINT, 330 months is the correct answer
