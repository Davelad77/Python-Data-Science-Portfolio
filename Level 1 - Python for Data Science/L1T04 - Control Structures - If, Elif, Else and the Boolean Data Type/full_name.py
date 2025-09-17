# program to validate the users enters at least two names when asked for their full name
# request the user input their full name
# validate the input so that:
# something has been entered
# more than 4 characters have been entered
# fewer than 25 characters have been entered
# if the input is valid, thank the user printing the full name

full_name = input("Please enter your full name: ")
if full_name == "":
    print("You haven't entered anything, please enter your full name")
elif len(full_name) <= 4:
    print("Your full name is too short, please enter your full name")
elif len(full_name) >= 25:
    print("Your full name seems too long, please check and re-enter your full name")
else:
    print("Thank you, " + full_name)