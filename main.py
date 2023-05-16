from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
# money_machine.report()
coffee_maker=CoffeeMaker()
# coffee_maker.report()
is_on=True
menu=Menu()
while is_on:
    options=menu.get_items()
    choice=input(f"what would you like? ({options})").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

