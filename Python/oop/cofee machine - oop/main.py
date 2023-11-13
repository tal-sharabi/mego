# Import necessary classes from respective modules
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

# Create instances of the classes
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# Main program loop
while True:
    # Get user input for coffee selection or to turn off the machine
    customer_choice = input("Choose a coffee (latte/espresso/cappuccino) or type 'off' to turn off: ")

    # Check if the user wants to turn off the machine
    if customer_choice == "off":
        break

    # Find the selected drink from the menu
    selected_drink = menu.find_drink(customer_choice)

    # Check if resources are sufficient and process payment
    if coffee_maker.is_resource_sufficient(selected_drink) and money_machine.make_payment(selected_drink.cost):
        # Make coffee and serve the customer
        coffee_maker.make_coffee(selected_drink)

# End of the program
