# Imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


# Constants
EXIT = "off"
PRINT_REPORT = "report"


def start_coffee_machine():
    """Coffee machine start function."""
    print(logo)

    # Coffee maker object
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    coffee_machine_run = True
    while coffee_machine_run:
        user_choice = input(f"What would you like? ({menu.get_items()}): ")
        if user_choice != EXIT:
            if user_choice == PRINT_REPORT:
                coffee_maker.report()
                money_machine.report()
            else:
                item = menu.find_drink(user_choice)
                if item is not None \
                        and coffee_maker.is_resource_sufficient(item) \
                        and money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
        else:
            coffee_machine_run = False


# Start the coffee machine
start_coffee_machine()
