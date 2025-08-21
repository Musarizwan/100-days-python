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
profit = 0.0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    elif choice in MENU:
        drink = MENU[choice]
        ingredients = drink["ingredients"]

        # 1. Check resources
        enough = True
        for item in ingredients:
            if resources[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                enough = False
                break

        if enough:
            # 2. Process coins
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            money_received = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            cost = drink["cost"]

            # 3. Check transaction
            if money_received < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(money_received - cost, 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                profit += cost

                # 4. Make coffee
                for item in ingredients:
                    resources[item] -= ingredients[item]
                print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid option. Try again.")