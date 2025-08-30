import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors? \n"))

if choice == 0:
    print("You chose rock")
elif choice == 1:
    print("You chose paper")
else:
    print("You chose scissors")

compChoice = random.randint(0, 2)

if compChoice == 0:
    print("The computer chose rock")
elif compChoice == 1:
    print("The computer chose paper")
else:
    print("The computer chose scissors")

if choice == 0 and compChoice == 2:
    print("You win")
elif choice == 1 and compChoice == 0:
    print("You win")
elif choice == 2 and compChoice == 1:
    print("You win")
elif choice == compChoice:
    print("It was a tie")
elif choice > 2 or choice < 0:
    print("You chose an invalid number. You lose")
else:
    print("You lose")


