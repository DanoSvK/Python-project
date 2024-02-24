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


def check_resources(drink):
    no_ingredients = False
    missing_ingredient = ""
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if not resources[ingredient] >= ingredients[ingredient]:
            no_ingredients = True
            missing_ingredient = ingredient
            break
    if no_ingredients:
        print(f"Sorry there is not enough {missing_ingredient}.")
    else:
        check_coins(drink)
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]


def check_coins(drink):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted_coins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[drink]["cost"]
    change = inserted_coins - cost
    if cost == inserted_coins:
        print(f"Here is your {drink} ☕ Enjoy!")
        resources["money"] += cost
    elif cost < inserted_coins:
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {drink} ☕ Enjoy!")
        resources["money"] += cost
    else:
        print("Not enough money. Money refunded.")
    return inserted_coins - change


def show_report():
    unit = ""
    for resource in resources:
        if resource == "water" or resource == "milk":
            unit = "ml"
        elif resource == "coffee":
            unit = "g"
        elif resource == "money":
            unit = "$"
        print(f"{resource}: {resources[resource]}{unit}")


def coffee_machine():
    resources["money"] = 0
    machine_on = True
    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            show_report()
        elif order == "off":
            machine_on = False
            print("Machine is turned off.")
        else:
            check_resources(order)


coffee_machine()

