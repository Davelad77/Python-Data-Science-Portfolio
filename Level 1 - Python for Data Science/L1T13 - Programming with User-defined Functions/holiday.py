# Calculate a users total holiday cost inc. plane, hotel and car rental
# Get user inputs:
#   city_choice => their destination city (present options with different costs)
#   num_nights => duration of their stay
#   rental_days => number of days they will rent a car
# 
# Create 4 functions
#   plane_cost => take city_flight as an argument and return the cost (use if/else)
#   hotel_cost => take num_nights as an argument, multiply it by nightly cost and return a total cost for the hotel stay
#   car_rental => take rental_days as an argument and return the cost 
#   holiday_cost => takes the three user defined inputs as arguments and calls the hotel_cost, plane_cost and car_rental functions
#                   with their respective arguments and finally returns the total cost for the holiday
# Print all details of the holiday in an easy to read format

# I had quite a lot of help from chatGPT whilst debugging the code below. I think it's probably over complicated in terms of variable
# naming conventions but I'm still getting to grips with lists and dictionaries so need to keep practicing that topic

# I chose to pull the selections from a file even though it made the task more complex as that felt more like something a company would do to allow for
# more destinations to be added without the need to change the code so future proofing the program to a degree

def plane_cost(destination_choice):
    if destination_choice in city_data_dict:
        return city_data_dict[destination_choice]["city_flight_cost"]       # Returns the cost of the flight that is stored in the dictionary against key = destination choice
    else:
        print("Invalid selection, please choose from the list")     # Prints a message but returns nothing so terminating the program
    
def hotel_cost(num_nights):     
    return num_nights * 200     # Calls the variable num_nights and multiplies it by the cost per night of the hotel returning the total
    
def car_rental(rental_days):
    return rental_days * 100     # Calls the variable rental_days and multiplies it by the cost per day of car hire returning the total

def holiday_cost(destination_cost, total_hotel_cost, total_car_rental):
    return destination_cost + total_hotel_cost + total_car_rental       # Calls the calculated variables returning their sum

with open('cities.txt', 'r') as file:       # Open the city pricing reference file
    lines = file.readlines()        # Read the lines of the file into a variable called lines

split_city_data = [s.split(';') for s in lines]     # Split the lines into substrings
city_data_dict = {}     # Create an empty dictionary to store the split city data

# Loop through each split substring to dynamically assign to variables
for x, city_data_sublist in enumerate(split_city_data):
    selection = int(city_data_sublist[0])
    city = city_data_sublist[1]
    city_flight_cost = int(city_data_sublist[2])

    #Store the values extracted above in the dictionary using keys 'selection', 'city' and 'city_flight_cost'
    city_data_dict[f"city_choice_{x}"] = {
        "selection": selection,
        "city": city,
        "city_flight_cost": city_flight_cost
    }

# Print the list of cities and the cost of flying to each in a simple list
print("Available Destinations are:")
for x in range(len(split_city_data)):
    print(x + 1, city_data_dict[f"city_choice_{x}"]["city"], city_data_dict[f"city_choice_{x}"]["city_flight_cost"])

print()

# Get user input
user_city_selection = int(input("Please enter the number of the city to which you would like to fly: ")) - 1        # Subtracts one from the user selection to account for indexing
if user_city_selection < 0 or user_city_selection > len(split_city_data) - 1:       # Performs a validity check on the user input
    print("Invalid selection, please run the program again")        # Terminates the program if invalid input
else:       # continues if the input is valid
    destination_choice = f"city_choice_{user_city_selection}"       # Selects the city based on the key set as the user_city_selection
    destination_cost = plane_cost(destination_choice)       # Sets the variable destination_cost to the returned value of the plane_cost function
    print()

    num_nights = int(input("Please enter the number of nights you wish to stay: "))
    total_hotel_cost = hotel_cost(num_nights)       # Sets the variable total_holiday_cost to the returned value of the function hotel_cost
    print()

    rental_days = int(input("Please enter the number of days you wish to rent a car: "))
    total_car_rental = car_rental(rental_days)      # Sets the variable total_car_rental to the returned value of the car_rental
    print()

    total_holiday_cost = holiday_cost(destination_cost, total_hotel_cost, total_car_rental)     # Sets the variable total_holiday_cost to the returned value of the function holiday_cost

    print(f"The cost of your flights is: ${destination_cost}")
    print(f"The cost of your hotel at $200 per night is: ${total_hotel_cost}")
    print(f"The cost of your car hire at $100 per day is: ${total_car_rental}")
    print(f"The cost of your holiday will be: ${total_holiday_cost}")
