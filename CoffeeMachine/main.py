# Constants
EXIT = "off"
PRINT_REPORT = "report"

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01

# Coffee machine data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(water, milk, coffee, machine_money):
    """Print the current status report of the machine."""
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${machine_money}")


def check_resources(water, milk, coffee, user_choice):
    """Check whether the coffee machine resources are enough to fulfill the user choice."""
    is_resources_enough = True;
    choice = MENU[user_choice]["ingredients"]
    if choice["water"] > water:
        print("Sorry there is not enough water.")
        is_resources_enough = False
    elif "milk" in choice and choice["milk"] > milk:
        print("Sorry there is not enough milk.")
        is_resources_enough = False
    elif choice["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        is_resources_enough = False
    return is_resources_enough


def handle_coins(user_choice):
    """Responsible for handling the coins."""
    choice = MENU[user_choice]

    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))

    total = (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNIE)

    coffee_cost = choice["cost"]
    if total >= coffee_cost:
        change = total - coffee_cost
        print(f"Here is ${change} dollars in change.")
        return coffee_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def start_coffee_machine():
    """Coffee machine start function."""

    # Initialize variables
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    money = 0

    coffee_machine_run = True
    while coffee_machine_run:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice != EXIT:
            if user_choice == PRINT_REPORT:
                print_report(water_level, milk_level, coffee_level, money)
            else:
                if user_choice in MENU:
                    if check_resources(water_level, milk_level, coffee_level, user_choice):
                        coffee_amount = handle_coins(user_choice)
                        if coffee_amount > 0:
                            money += coffee_amount

                            choice_ingredients = MENU[user_choice]["ingredients"]
                            water_level -= choice_ingredients["water"]
                            if "milk" in choice_ingredients:
                                milk_level -= choice_ingredients["milk"]
                            coffee_level -= choice_ingredients["coffee"]

                            print(f"Here is your {user_choice} ☕. Enjoy")
                else:
                    print(f"User choice: {user_choice} is invalid and please retry!")
        else:
            coffee_machine_run = False


# Start the coffee machine
start_coffee_machine()

