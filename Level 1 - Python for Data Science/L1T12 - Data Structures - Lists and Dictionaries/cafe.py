# create a list called menu
# create a dictionary called stock which should contain the stock value for each item on the menu
# create another dictionary called price which should contain the prices for each item on the menu
# calculate the total stock value in the cafe
#   use loops through the relevant dictionaries and lists

menu = ["coffee", "tea", "apple juice", "sandwich", "crisps", "cake"]

stock = {
    "coffee": 20,
    "tea": 40,
    "apple juice": 50,
    "sandwich": 100,
    "crisps": 200,
    "cake": 150
}

price = {
    "coffee": 2.5,
    "tea": 1.5,
    "apple juice": 0.5,
    "sandwich": 4.0,
    "crisps": 1.0,
    "cake": 3.0
}
# calculate the total stock value in the cafe
total_stock_value = 0
for item in menu:
    total_stock_value += stock[item] * price[item]
    item_value = stock[item] * price[item]
    print(f"The value of {item} is {item_value}")

print()
print("Total stock value in the cafe: £", total_stock_value)
