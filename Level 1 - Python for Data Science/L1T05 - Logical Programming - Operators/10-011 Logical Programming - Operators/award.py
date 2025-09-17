# program to determine the category a competitor will achieve after completing a triathlon
# request the finishing time in minutes for each discipline (swim, bike and run)
# calculate the total time and determine the category based on the following:
# National colours: 100 minutes or less
# County colours: 101 to 105 minutes
# Club colours: 106 to 110 minutes
# Finisher: 111+ minutes
# display the category the competitor has achieved

swim_time = int(input("Enter the swim time in minutes: "))
bike_time = int(input("Enter the bike time in minutes: "))
run_time = int(input("Enter the run time in minutes: "))
total_time = swim_time + bike_time + run_time
if total_time <= 100:
    print(f"Awesome work, you made 'National colours' by finishing in {total_time} mins")
elif total_time >= 101 and total_time <= 105:
    print(f"Great effort, you made 'County colours' by finishing in {total_time} mins")
elif total_time >= 106 and total_time <= 110:
    print(f"Good job, you receive 'Club colours by finishing in {total_time} mins")
else:
    print(f"Well done for finishing in {total_time} mins")
