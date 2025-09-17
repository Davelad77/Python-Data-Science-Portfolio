# read data from text file DOB.txt in the same folder
# print out the contents in two different sections:
# section 1 - Name
# section 2 - Birthdate

with open('DOB.txt', 'r') as f:     # opens the file safely so it closed automatically when the program concludes
    dob_data = f.readlines()        # reads each line of data into the variable 'dab_data'


split_dob_data = [s.split() for s in dob_data]      # split the individual strings inside the list of dob_data into substrings

print("----- Name -----")
for i in range(len(split_dob_data)):
    name = " ".join(split_dob_data[i][0:2])        # create a new variable called name to store the items in the list joined as a single string with a space
    print(name)

print()

print("----- Date of Birth -----")
for i in range(len(split_dob_data)):
    dob = " ".join(split_dob_data[i][2:])        # create a new variable called dob to store the items in the list joined as a single string with a space
    print(dob)
