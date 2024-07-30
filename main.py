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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, false if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
     """Returns the total calculated from coins inserted."""
     print("Please insert coins.")
     total1 = int(input("How many quarters?: ")) * 0.25
     total2 = int(input("How many dimes?: ")) * 0.1
     total3 = int(input("How many nickles?: ")) * 0.05
     total4 = int(input("How many pennies?: ")) * 0.01
     sum = total1 + total2 + total3 + total4
     return sum

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name , order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

print(logo)
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources["water"]}")
        print(f"milk: {resources["milk"]}")
        print(f"coffee: {resources["coffee"]}")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])