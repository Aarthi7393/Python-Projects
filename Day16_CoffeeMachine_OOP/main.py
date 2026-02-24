from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_making = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_machine_on = True
while is_machine_on:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee_making.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_making.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_making.make_coffee(drink)

