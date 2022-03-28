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

machine_on = True


def check(drink):
    water_left = water_remaining - MENU[drink]['ingredients']['water']
    if water_left < 0:
        print("Sorry there is not enough water.")
        return False
    milk_left = milk_remaining - MENU[drink]['ingredients']['milk']
    if milk_left < 0:
        print("Sorry there is not enough milk.")
        return False
    coffee_left = coffee_remaining - MENU[drink]['ingredients']['coffee']
    if coffee_left < 0:
        print("Sorry there is not enough coffee.")
        return False
    return True


def payment(drink):
    if money_collected >= MENU[drink]['cost']:
        change = money_collected - MENU[choice]['cost']
        change_2dp = round(change, 2)
        print(f"Here is ${change_2dp} dollars in change.")
        print(f"Here is your {drink}. Enjoy! ")
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


water_remaining = 300
milk_remaining = 200
coffee_remaining = 100
money = 0


while machine_on:

    report = f"Water: {water_remaining}ml, Milk: {milk_remaining}ml, Coffee: {coffee_remaining}g, Money: ${money}"

    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == 'report':
        print(report)
    elif choice == 'off':
        machine_on = False
        print("Have a nice day.")
    elif choice == 'espresso':
        if check(choice):
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            money_collected = float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
            if payment(choice):
                money += MENU[choice]['cost']
                water_remaining -= 50
                coffee_remaining -= 18
        else:
            print("machine out of order")
    elif choice == 'latte':
        if check(choice):
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            money_collected = float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
            if payment(choice):
                money += MENU[choice]['cost']
                water_remaining -= 200
                milk_remaining -= 150
                coffee_remaining -= 24
        else:
            print("machine out of order")
    elif choice == 'cappuccino':
        if check(choice):
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            money_collected = float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
            if payment(choice):
                money += MENU[choice]['cost']
                water_remaining -= 250
                milk_remaining -= 100
                coffee_remaining -= 24
        else:
            print("machine out of order")

