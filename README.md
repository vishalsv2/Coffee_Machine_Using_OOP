# Coffee_Machine_Using_OOP
A Python program that simulates a coffee machine. The user can choose from a menu of coffee drinks, and the machine will make the coffee 
if it has the necessary resources and the user pays the correct amount using oop.

# Coffee Machine

This is a simple program that simulates a coffee machine. It allows the user to choose from three types of coffee: espresso, latte, and 
cappuccino. It also keeps track of the resources and money in the machine.

# How to run

To run the program, you need Python 3 installed on your computer. You also need to download the files `menu.py`, `coffee_maker.py`, and 
`money_machine.py` from this repository. Then, you can run the file `main.py` in your terminal or IDE.

# How to use

When you run the program, you will see a prompt asking you what would you like to order. You can type one of the following options:

- `espresso`: This will make an espresso for you. It costs $1.5 and uses 50 ml of water, 18 g of coffee beans, and no milk.
- `latte`: This will make a latte for you. It costs $2.5 and uses 200 ml of water, 24 g of coffee beans, and 150 ml of milk.
- `cappuccino`: This will make a cappuccino for you. It costs $3 and uses 250 ml of water, 24 g of coffee beans, and 100 ml of milk.
- `off`: This will turn off the machine and exit the program.
- `report`: This will show you the current status of the resources and money in the machine.

After you type your choice, the program will check if there are enough resources to make your drink. If there are, it will ask you to insert coins
to pay for it. You can insert quarters ($0.25), dimes ($0.1), nickels ($0.05), and pennies ($0.01). The program will calculate the total amount
of money you inserted and compare it with the cost of the drink. If you inserted enough money, it will make your drink and give you change if any.
If you inserted too little money, it will refund your coins and ask you to try again.

The program will repeat this process until you choose to turn off the machine or until it runs out of resources.

# Modules

The program uses three modules that are imported from separate files:

- `menu.py`: This module contains the class `Menu`, which has methods to get the items, prices, and ingredients of the drinks.
  It also contains the class `MenuItem`, which represents each drink as an object with attributes such as name, cost, and ingredients.
- `coffee_maker.py`: This module contains the class `CoffeeMaker`, which has methods to check if there are enough resources to make a drink,
  deduct the resources used for a drink, and report the current resources in the machine.
- `money_machine.py`: This module contains the class `MoneyMachine`, which has methods to accept coins from the user, calculate the total amount of money inserted,
  check if the payment is sufficient for a drink, process the payment and give change if any, and report the current money in the machine.

