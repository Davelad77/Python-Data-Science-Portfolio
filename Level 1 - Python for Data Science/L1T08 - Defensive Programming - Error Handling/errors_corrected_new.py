# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")        # SYNTAX ERROR - missing parentheses
print("\n")      # SYNTAX ERRORS - unexpected indent and missing parentheses

# SYNTAX ERRORS - each of the next 5 lines of code are incorrectly indented

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"       # RUNTIME ERROR - using == is a test not a way to define a variable
age = int(age_Str[0:2])      # RUNTIME ERROR - age_Str is a string so cannot be cast as an int, need to splice the string to leave the integer
print(f"I'm {age} years old.")   # RUNTIME ERROR - have to use an f-string to concatenate a non-string variable

# Variables declaring additional years and printing the total years of age
years_from_now = 3        # RUNTIME ERROR - Surrounding the number 3 in " saves the variable as a string so cannot be used in calculations
total_years = age + years_from_now

# The end of the unexpected indent SYNTAX ERRORS

print(f"The total number of years: {total_years}")        # SYNTAX ERROR - missing parentheses and answer_years not defined
                                                        # RUNTIME ERROR - enclosing answer_years in " prints that as text and need to use f-string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12      # RUNTIME ERROR - wrong variable name used, should be total_years
print(f"In 3 years and 6 months, I'll be {total_months + 6} months old")       # SYNTAX ERROR - missing parentheses
                                                                               # RUNTIME ERROR - have to use an f-string to concatenate a non-string variable

# LOGIC ERROR - The result specifies 3 years and 6 months but the calculations don't incude the additional 6 months

#HINT, 330 months is the correct answer
