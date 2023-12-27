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

def is_resources_sufficient(order_ingredients):

    for ingredients in order_ingredients:
        if order_ingredients[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {ingredients}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? :")) * 0.25
    total = int(input("How many dimes? :")) * 0.10
    total = int(input("How many nickle? :")) * 0.05
    total = int(input("How many pennis? :")) * 0.01
    return total

def is_transaction_successful(payment, cost):
    if payment > cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(user, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {user} ☕️. Enjoy!")


is_machine_turn_on = True

while is_machine_turn_on:
    user = input("What would you like? (espresso/latte/cappuccino)"
                 "if you want to turning off/report:").lower()
    if user == 'off':
        is_machine_turn_on = False
    elif user == 'report':
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
    else:
        drink = MENU[user]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user, drink['ingredients'])