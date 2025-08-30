def main():
    score = int(input("Enter your score here: "))

    if (score >=90):
        return("A")
    elif (score >=80):
        return("B")
    elif (score >=70):
        return("C")
    elif (score >=60):
        return("D")
    else:
        return("F")

print(f"Your grade is: {main()}")