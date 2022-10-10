from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffee_make = CoffeeMaker()
my_menu = Menu()

machine_on = True
while machine_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}report/off): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        my_coffee_make.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_make.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_make.make_coffee(drink)





