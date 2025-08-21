☕ Coffee Machine Simulation (Python)

This is a Python terminal-based coffee machine program.
It simulates how a real coffee vending machine works by:

   Offering drinks (espresso, latte, cappuccino)

   Checking if resources (water, milk, coffee) are sufficient

   Processing coin input (quarters, dimes, nickels, pennies)

   Giving change if needed

   Updating resources and tracking profit

Features

  Menu options: espresso, latte, cappuccino

  Type report to view remaining resources and profit

  Type off to shut down the machine

  Resource tracking (water, milk, coffee)

  Handles real-world coin denominations

  Refunds money if not enough is provided

  Deducts resources only after a successful transaction

Gameplay Flow

 User selects a drink: espresso, latte, or cappuccino.

 Machine checks if enough water, milk, and coffee are available.

 If enough → prompts user to insert coins.

 Machine calculates total money:

     Quarters ($0.25)

     Dimes ($0.10)

     Nickels ($0.05)

     Pennies ($0.01)

If money < cost → refund given.

If money >= cost → gives change (if any), updates profit, and serves drink.

Type report anytime to view resources and profit.

Type off to turn off the machine.

Example Run
  What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 8
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 dollars in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
