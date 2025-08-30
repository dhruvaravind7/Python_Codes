import Blackjack_Art
import random

print(Blackjack_Art.logo)

def GenerateCard():
    position = random.randint(0, len(cards)-1)
    return(cards[position])

def CardSum(list):
    sum = 0
    for i in list:
        sum += i
    return(sum)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = []
computerCards = []

playerCards.append(GenerateCard())
playerCards.append(GenerateCard())
computerCards.append(GenerateCard())
computerCards.append(GenerateCard())



playerSum = CardSum(playerCards)
computerSum = CardSum(computerCards)

continueGame = True

print(f"Your cards: {playerCards}, current score: {playerSum}")
print(f"Computer's first card: {computerCards[0]}\n")
while continueGame == True:
    newCard = input("Type 'y' to get another card, type 'n' to pass: ")
    if newCard == "y":
        playerCards.append(GenerateCard())
    else:
        continueGame = False
    print(f"\nYour cards: {playerCards}, current score: {CardSum(playerCards)}")
    print(f"Computer's first card: {computerCards[0]}\n")  
    if CardSum(playerCards) > 21:
        continueGame = False

while CardSum(computerCards) < 17:
    computerCards.append(GenerateCard())


playerSum = CardSum(playerCards)
computerSum = CardSum(computerCards)

print(f"Your final hand: {playerCards}, final score: {playerSum}")
print(f"Computer's final hand: {computerCards}, final score {computerSum}\n")

if playerSum > 21:
    print("You went over. You Lose")
elif computerSum > 21:
    print("The dealer went over. You Win!!!")
elif playerSum > computerSum:
    print("Your score was higher. You Win!!!")
else:
    print("Your score was lower. You Lose")