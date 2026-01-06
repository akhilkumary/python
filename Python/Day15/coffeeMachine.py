QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.50
    }
}

CAPACITY = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

resources = {
    "ingredients": CAPACITY,
    "money": 0
}

# TODO3: Report with ingredients (water, milk, coffee) and money in the machine
def printReport(res):
    for k in res:
        if k == "ingredients":
            for r in res[k]:
                print(f"{r.title()}: {res[k][r]} {'g' if r == 'coffee' else 'ml'}")
        else:
            print(f"{k.title()}: ${res[k]}")

# TODO4: After user choice, check for sufficent resources to make that drink
def checkResources(res, choice, m):
    for item in m:
        if item == choice:
            for ing in m[item]['ingredients']:
                if res['ingredients'][ing] < m[item]['ingredients'][ing]:
                    return ing
            return "sufficient"
    return "out"

# TODO6: Transaction success
def checkTransaction(choice, amount, m):
    for item in m:
        if item == choice:
            if amount < m[item]['price']:
                return False
    return True
    # if amount < MENU[choice]['price']: return False
       
# TODO7: Make Coffee - Resource deduction on machine and prompt to user
def updateMachineResources(resources, user_choice, amt, m):
    for res in resources:
        if res == 'ingredients':
            for ing in m[user_choice][res]:
                resources[res][ing] -= m[user_choice][res][ing]
        elif res == 'money':
            resources[res] += round(m[user_choice]['price'], 2)
    return round(amt - m[user_choice]['price'], 2)

# TODO1: Prompt the user with the choices of coffee
coffee_machine = 'on'

# TODO2: Handle turning off the coffee machine (Maintainers of coffe machine - no separate prompt)
while coffee_machine == 'on':
    
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'report':
        printReport(resources)
        continue

    if user_choice == 'off':
        coffee_machine = 'off'
        break

    res_check = checkResources(resources, user_choice, MENU)
    if res_check == 'sufficient':
        # TODO5: Prompt for Processing coins - Quarters, Dimes, Nickles, Pennies
        print("Please insert the coins.")
        quarters = int(input("Number of quarters: "))
        dimes = int(input("Number of dimes: "))
        nickles = int(input("Number of nickles: "))
        pennies = int(input("Number of pennies: "))

        amt = quarters*QUARTER + dimes*DIME + nickles*NICKLE + pennies*PENNY
        # TODO6: Transaction success
        if checkTransaction(user_choice, amt, MENU):

            change = updateMachineResources(resources, user_choice, amt, MENU)
            if change > 0:
                print(f"Here is ${change} dollars in change.")
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(f"Sorry that's not enough money. Money refunded.")
    elif res_check == 'out':
        print(f"Invalid Choice! Choose from the menu.")
    else:
        print(f"Sorry there is not enough {res_check}.")