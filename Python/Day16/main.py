from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMenu = Menu()
coffeeMachine = CoffeeMaker()
moneyCounter = MoneyMachine()

while True:

    user_choice = input(f"What would you like? {coffeeMenu.get_items()}: ").lower()

    if user_choice == 'report':
        coffeeMachine.report()
        moneyCounter.report()
        continue

    if user_choice == 'off':
        break

    if coffeeMachine.is_resource_sufficient(coffeeMenu.find_drink(user_choice)):
        if moneyCounter.make_payment(coffeeMenu.find_drink(user_choice).cost):
            coffeeMachine.make_coffee(coffeeMenu.find_drink(user_choice))