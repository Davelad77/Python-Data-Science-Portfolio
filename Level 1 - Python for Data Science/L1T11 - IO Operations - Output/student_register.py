# write a program that allows students to register for an exam
# ask the user how many students are registering (x)
# create a for loop to run x times
# each time the loop runs ask the user to enter the next student ID
# write each student ID to a txt file called reg_form.txt
# include a dotted line between student names to allow the document to be used as a register

num_students = int(input("Please enter the number of students registered for the exam: "))      # request the number of students but cast as an int

i = 0       #set counter to zero

with open('reg_form.txt', 'a') as f:      # open a file in the same dir called output.txt and create if not present
    for i in range(num_students):      #loop the following commands the number of times there are students
        student_ID = input("Please enter the next student ID: ")
        f.write(student_ID + "\n")          # append the next student ID to the reg_form.txt file 
        f.write("--------------------\n")       # append a dotted line underneath the student ID

