from art import logo

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_report():
    """Print current report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(left_resources, coffee_name):
    """Returns True when order can be made, False if resources are insufficient."""
    is_enough = True
    for item in left_resources:
        if left_resources[item] < MENU[coffee_name]["ingredients"][item]:
            print(f"Sorry there is no enough {item}.")
            is_enough = False
    return is_enough  # return should be the end of the function


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return money


def coffee_make(payment, coffee_name, left_resources):
    cost = MENU[coffee_name]["cost"]
    if cost > payment:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(payment - cost, 2)
        for item in left_resources:
            left_resources[item] -= MENU[coffee_name]["ingredients"][item]
        print(f"Here is ${change} in change.\nHere is your {choice} ☕️. Enjoy!")
        global profit
        profit += cost


machine_on = True
while machine_on:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ")
    if choice == "off":
        machine_on = False
        break
    elif choice == "report":
        check_report()
    else:
        make_one_coffee = is_resource_sufficient(resources, choice)
        while make_one_coffee:
            user_money = process_coins()
            coffee_make(user_money, choice, resources)
            make_one_coffee = False

