# This is a program written as solution to the Compulsory Task 1 of the Capstone Project

#=====importing libraries===========
'''This is the section where you will import libraries'''

with open('user.txt', 'r') as user_file:
    users = user_file.readlines()   # Create a list containing the users in the file

user_list = [user.replace(' ', '').strip().split(',') for user in users]    # Create a list of lists containing the users in the file
user_list_dict = {user[0]: user[1] for user in user_list}   # Create a dictionary containing the users in the file

with open('tasks.txt', 'r') as task_file:
    tasks = task_file.readlines()   # Create a list containing the tasks in the file

task_list = [task.strip().split(',') for task in tasks]    # Create a list of lists containing the tasks in the file
task_list_dict = {}
keys = ['assigned_user', 'task_title', 'task_description', 'current_date', 'due_date', 'task_status']   # Create a list of keys for the dictionary

for task in task_list:
    task_list_dict[task[0]] = {keys[i]: task[i] for i in range(6)}   # Create a dictionary containing the tasks in the file

import textwrap

#====Login Section====
'''Code that will allow a user to login.
    - Read username and password from the user.txt file
    - Use a dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate the user name and password
'''

username = input('Please enter your username: ')
password = input('Please enter your password: ')
print()

if username in user_list_dict and user_list_dict[username] == password:
    print('Login successful')
else:
    print('Login unsuccessful - please try again')
    print('Please note, userIDs are case sensitive')
    exit()

print()


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    
    print()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        new_username = input('Enter a new username: ')
        new_password = input('Enter a new password: ')
        confirm_password = input('Please re-enter your password: \n')
        if new_password == confirm_password:
            with open('user.txt', 'a') as user_file:
                user_file.write(f'\n{new_username}, {new_password}')
                print('User successfully registered\n')
        else:
            print('Passwords do not match. Please try again\n')
        with open('user.txt', 'r') as user_file:        # Re-read the user file to update with the new user
            users = user_file.readlines()
        user_list = [user.replace(' ', '').strip().split(',') for user in users]    # Re-create the list of lists containing the updated users in the file
        user_list_dict = {user[0]: user[1] for user in user_list}   # Re-create the dictionary containing the updated users in the file


    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to checking that the username is in the user.txt file,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

        assigned_user = input('To which userID should the task be assigned? ')
        if assigned_user not in user_list_dict:     # Check if the user exists
            print('\nThis user does not exist. Please try again using one of the below users or add a new user\n')
            for user in user_list:
                print(f'{user[0]}')      # Print the list of users for reference
            print()
            continue
        
        task_title = input('Please enter a title for the task: ')
        task_description = input('Please enter a brief description of the task: ')
        due_date = input('Please enter the due date for the task (YYYY-MM-DD): \n')

        from datetime import date
        current_date = date.today()    # Get the current date

        with open('tasks.txt', 'a') as task_file:
            task_file.write(f'\n{assigned_user}, {task_title}, {task_description}, {current_date}, {due_date}, No')   # Add the task to the file
            print('Task successfully added\n')
        with open('tasks.txt', 'r') as task_file:       # Re-read the task file to update with the new task
            tasks = task_file.readlines()
            task_list = [task.strip().split(',') for task in tasks]    # Re-create the list of lists containing the tasks in the file
            task_list_dict = {}
            keys = ['assigned_user', 'task_title', 'task_description', 'current_date', 'due_date', 'task_status']   # Re-create the list of keys for the dictionary
            for task in task_list:
                task_list_dict[task[0]] = {keys[i]: task[i] for i in range(6)}   # Re-create the dictionary containing the tasks in the file

    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        for task in task_list:
            print('-' * 20)
            print(textwrap.dedent(f"""
            Task : {task[1]}
            Task assigned to: {task[0]}
            Date assigned: {task[3]}
            Due date: {task[4]}
            Task complete? {task[5]}
            Task description: {task[2]}
            """))
        print('-' * 20)
        print()


    elif menu == 'vm':
        '''This code block will read the tasks from task.txt file and split them into a dictionary
            - For each task in the list of tasks:
            - Check if the username of the person logged in is the same as the 
              username to whic the task has been assigned
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

        for task in task_list:
            if task[0] == username:
                print('-' * 20)
                print(textwrap.dedent(f"""
                Task : {task[1]}
                Task assigned to: {task[0]}
                Date assigned: {task[3]}
                Due date: {task[4]}
                Task complete? {task[5]}
                Task description: {task[2]}
                """))
                print('-' * 20)
            print()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
