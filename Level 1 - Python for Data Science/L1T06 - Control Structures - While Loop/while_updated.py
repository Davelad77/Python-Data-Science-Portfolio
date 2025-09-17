# ask the user to enter a number
# keep asking the user to enter a number until the user enters -1
# once the user enters -1 calculate the average of the entered numbers excluding -1
# Display the average

user_num = 0
counter = 1
total_user_num = 0

while user_num != -1:
    user_num = int(input("Please enter a number (-1 to finish): "))
    if user_num == -1:      # Add control to exit the program without any runtime errors if the user enters -1 straight away
        print(f"Your final average is: {avg}, thankyou goodbye")
        break       # If the user enters -1 straight away stop the while loop from processing
    else:
        total_user_num += user_num      # Add the user input the running total
        avg = (total_user_num) / (counter)      # Calculate the current average
        counter += 1        # Increment the counter
        print(f"The average of your numbers is: {avg}\n")
