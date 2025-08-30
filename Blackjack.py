# The two modules below were not written by me
import random
import os


def GenerateCard():
    numCards = 0
    for i in numOfEachCard:
        numCards += i
    position = random.randint(1, numCards)
    curCard = 0
    for j in range(0, len(numOfEachCard)):
        curCard += numOfEachCard[j]
        if curCard >= position:
            numOfEachCard[j] -= 1
            break
    return(cards[j])



def ConvertHand(hand):
    newHand = hand.copy()
    for i in range(0, len(newHand)):
        if newHand[i] == "A":
            newHand[i] = 11
        elif newHand[i] == "J" or newHand[i] == "Q" or newHand[i] == "K":
            newHand[i] = 10
    return(newHand)

# Calculates the total sum of all the cards in the hand
def CardSum(hand):
    sum = 0
    numAces = hand.count("A")
    newHand = ConvertHand(hand).copy()
    for i in newHand:
        sum += i
    if sum > 21 and numAces > 0:
        sum -= (10*numAces)
    return(sum)

moneyLeft = 100

numDecks = int(input("How many decks do you want to play with: "))
while True:
    numOfEachCard = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    numOfEachCard = [i * numDecks for i in numOfEachCard]



    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    
    os.system('clear||cls')
    playerCards = []
    computerCards = []


    playerCards.append(GenerateCard())
    playerCards.append(GenerateCard())
    computerCards.append(GenerateCard())
    computerCards.append(GenerateCard())
    playerSum = CardSum(playerCards)
    computerSum = CardSum(computerCards)
    ########
    continueGame = True

    # Ensures that a valid bet amount is placed
    exitLoop = False
    while True:
        OppDraw = True
        blackJackAttained = False

        if exitLoop == True:
            break
        betAmount = int(input(f"\nYou currently have ${moneyLeft}. How much money do you want to bet: $"))
        exitLoop = True
        if betAmount > moneyLeft:
           print("You do not have that much money.")
           exitLoop = False
        if isinstance(betAmount, int) == False:
            print("Please add a whole number")
            exitLoop = False
        if betAmount < 0:
            print("You cannot bet a negative value")
            exitLoop = False
        
    # Subtracts the amount you bet from your total
    moneyLeft -= betAmount

    # Prints the visible cards and checks if you have a blackjack
    print(f"\nYour cards: {playerCards}, current total: {playerSum}")
    print(f"Computer's first card: {computerCards[0]}")
    if playerSum == 21:
        moneyLeft += betAmount
        moneyLeft += int((betAmount*1.5))
        print("BLACKJACK!!!")
        blackJackAttained = True
        OppDraw = False
    
    counter = 0
    while continueGame == True:
        if blackJackAttained:
            break
        counter += 1
        newCard = input("\nType 'h' to hit another card, type 's' to stand, or 'd' to double: ")
        if newCard == "h":
            playerCards.append(GenerateCard())
        elif newCard == "d":
            if moneyLeft - betAmount < 0:
                print("\nYou don't have enough money to double")
                continue
            if counter > 1:
                print("\nYou can only double on the first card")
                continue
            moneyLeft -= betAmount
            betAmount *= 2
            playerCards.append(GenerateCard())
            continueGame = False
        else:
            continueGame = False
            continue
        print(f"\nYour cards: {playerCards}, current total: {CardSum(playerCards)}")
        print(f"Computer's first card: {computerCards[0]}")  
        if CardSum(playerCards) >= 21:
            continueGame = False
            OppDraw = False


    if OppDraw == True:
        while CardSum(computerCards) < 17 or (CardSum(computerCards) == 17 and computerCards.count(11) == 1):
            computerCards.append(GenerateCard())


    playerSum = CardSum(playerCards)
    computerSum = CardSum(computerCards)

    if blackJackAttained == False:
        print(f"\nYour final hand: {playerCards}, final total: {playerSum}")
        print(f"Computer's final hand: {computerCards}, final total {computerSum}\n")

        if playerSum > 21:
            print("You went over. You Lose")
        elif computerSum > 21:
            print("The dealer went over. You Win!!!")
            moneyLeft += (2*betAmount)
        elif playerSum > computerSum:
            print("Your total was higher. You Win!!!")
            moneyLeft += (2*betAmount)
        elif playerSum == computerSum:
            print("You pushed.")
            moneyLeft += betAmount
        else:
            print("Your total was lower. You Lose")

    if moneyLeft <= 0:
        break
    playAgain = input(f"\nYou have ${moneyLeft} left. Type 'y' to play again or 'n' to cash out: ")
    if playAgain == "n":
        break

print(f"\nYour final total is ${moneyLeft}")
    
