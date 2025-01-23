from budgetFunction import budgetFunction
from calculator import calculator, add
from weather import weathers 
from shopping_list import shopping_lists
from TemperatureConverter import celsius_to_fahrenheit
from TemperatureConverter import fahrenheit_to_celsius
from inventory import inventorys
from password import validate_password
# Create a Function: Turn this logic into a function called suggest_destination(budget) that:

# Accepts budget as an argument.
# Returns the suggestion as a string.


print(budgetFunction(300))
print(calculator(10,5))
print(add(10,5))
print(weathers("rainy"))
print(shopping_lists("carrotss"))
print(celsius_to_fahrenheit(10))
print(fahrenheit_to_celsius(60))
print(inventorys("apples"))
print(validate_password(13))

# Instructions for Students:

# Refactor this code by creating a function for each arithmetic operation (e.g., add, subtract, etc.).
# Make a Calculator class that contains these functions as methods.
# Ensure that division checks for zero before attempting the operation.
# Move the arithmetic logic into a file named calculator.py.

####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.


# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.


# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.





# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.









# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.

