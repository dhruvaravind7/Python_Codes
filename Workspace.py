def CardSum(hand):
    sum = 0
    numAces = hand.count("A")
    #hand = list(map(lambda x: x.replace('A', "B"), hand))
    if numAces > 0:
        hand[hand.index("A")] = 11
    for i in hand:
        sum += i
    if sum > 21 and numAces > 0:
        sum -= (10*numAces)
    #hand = list(map(lambda x: x.replace(11, "A"), hand))
    return(sum)

print(CardSum(["A", 9, 9]))