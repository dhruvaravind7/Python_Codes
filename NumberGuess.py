import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number from 1 and 100")

win = False
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
if difficulty == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        win = True
        break
    if lives != 1:
        print("Guess again")
    lives -= 1  

if win == True:
    print(f"You got it right!")
else:
    print(f"You lose. The number was {number}")