import random
from turtle import position
import HigherLower_Art
from HigherLower_Data import data
import os

print(HigherLower_Art.logo)
positionA = random.randint(0, len(data)-1)
score = 0

while True:
    while True:
        positionB = random.randint(0, len(data)-1)
        if positionB != positionA:
            break

    if data[positionA]["follower_count"] > data[positionB]["follower_count"]:
        moreFollowers = "A"
    else:
        moreFollowers = "B"
    
    print("Compare A: " + data[positionA]["name"] + ", a " + data[positionA]["description"] + ", from " + data[positionA]["country"], end="\n\n")
    print(HigherLower_Art.vs, end="\n\n")
    print("Against B: " + data[positionB]["name"] + ", a " + data[positionB]["description"] + ", from " + data[positionB]["country"], end="\n\n")

    decision = input("Who has more followers? Type 'A' or 'B': ").strip().title()
    if decision != moreFollowers:
        break
    else: 
        os.system("cls")
        score += 1
        print(HigherLower_Art.logo, end = "\n\n")
        print(f"You're right! Current score: {score}.")
        positionA = positionB
os.system("cls")
print(HigherLower_Art.logo, end = "\n")
print(f"Sorry that's wrong. Final score: {score}")