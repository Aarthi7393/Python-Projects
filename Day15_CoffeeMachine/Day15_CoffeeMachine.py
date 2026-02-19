MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def resource_detection(user_resource):
    print(f"Resource before deletion : {resources}")
    for key in user_resource:
        resources[key] -= user_resource[key]
    print(f"Resource after deletion : {resources}")



# TODO 5: Process coins quarter = 0.25, dimes = 0.10, nickles = 0.05 and penny = 0.01
def collect_money(cost):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    user_money = quarters * 0.25 +  dimes * 0.10 + nickels * 0.05  + pennies * 0.01
    print(f"You paid §{user_money:.2f}" )

    # TODO: If enough money, now detect the resources
    if user_money >= cost:
        bal_amt = user_money - cost
        if bal_amt > 0:
            print(f"Here is your balance amount ${bal_amt:.2f}")
    else:
        print("Sorry no enough money.Your money is refunded. Try another drink")
        return False
    return True



# TODO 4: Check if sufficient resource available
def check_resources(user_resource):
    print(user_resource)
    print(resources)

    for key in resources:
        if resources[key] < user_resource[key]:
            print("Sorry no enough resource. Try another drink")
            return False
    return True


def restock():
    restock_resources = {
    "water": 5000,
    "milk": 1000,
    "coffee": 300,
    }
    for key in restock_resources:
        resources[key] += restock_resources[key]


# TODO: Print report of available resources
def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Profit: {profit}")

is_machine_on = True
while is_machine_on:
    user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print_report()
    elif user_choice == "restock":
        restock()
    else:
        user_resource = MENU[user_choice]["ingredients"]
        if check_resources(user_resource):
            print("Resource available")
            print(f"The cost of the drink is ${MENU[user_choice]["cost"]}")
            if collect_money(float(MENU[user_choice]["cost"])):
                profit += float(MENU[user_choice]["cost"])
                resource_detection(user_resource)

