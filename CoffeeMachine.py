from re import M
from CoffeeMachine_Info import Menu
from CoffeeMachine_Info import Resources
import math

def report(Money):
    print(f"Water:", Resources["water"])
    print(f"Milk:", Resources["milk"])
    print(f"Coffee:", Resources["coffee"])
    print(f"Money: ${Money}")

def checkResources(action):
    work = True
    if Resources["water"] < Menu[action]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        work = False
    if Resources["milk"] < Menu[action]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        work = False
    if Resources["coffee"] < Menu[action]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        work = False
    return(work)


totalMoney = 0


while True: 
    balance = 0
    work = True

    action = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if action == "report":
        report(totalMoney)
        continue
    
    work = checkResources(action)
    if work == False:
        continue

    print("Please insert coins.")
    balance += 0.25* int(input("How many quarters? "))
    balance += 0.1* int(input("How many dimes? "))
    balance += 0.05* int(input("How many nickels? "))
    balance += 0.01* int(input("How many pennies? "))

    balance = round(balance, 2)

    if balance < Menu[action]["cost"]:
        print("Sorry thats not enough money. Money refunded. ")
        continue
    
    change = round(balance - Menu[action]["cost"], 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {action}. Enjoy")

    totalMoney += Menu[action]["cost"]
    Resources["water"] -= Menu[action]["ingredients"]["water"]
    Resources["milk"] -= Menu[action]["ingredients"]["milk"]
    Resources["coffee"] -= Menu[action]["ingredients"]["coffee"]