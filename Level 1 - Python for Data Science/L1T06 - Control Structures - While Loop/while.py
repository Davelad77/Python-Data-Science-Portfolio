# ask the user to enter a number
# keep asking the user to enter a number until the user enters -1
# once the user enters -1 calculate the average of the entered numbers excluding -1
# Display the average

user_num = 0
counter = 0
total_user_num = 0

while user_num != -1:
    user_num = int(input("Please enter a number (-1 to finish): "))
    total_user_num += user_num
    counter += 1
avg = (total_user_num + 1) / (counter - 1)
print(f"The average of your numbers is: {avg}")
