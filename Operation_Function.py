def Sum(Numbers):
    sum = 0
    for count in range(0,len(Numbers)):
        sum = sum + Numbers[count]
    print("The sum of the numbers is " + str(sum))

def LargestNumber(Numbers):
    LargestNumber = Numbers[0]
    for count in range(0,len(Numbers)):
        if LargestNumber < Numbers[count]:
            LargestNumber = Numbers[count]
    print("The largest number is " + str(LargestNumber))

def Squares(Numbers):
    SquareList = []
    for count in range(0, len(Numbers)):
        SquareList.append(Numbers[count]*Numbers[count])
    print("The square of all the numbers are: ")
    print(SquareList) 

def Average(Numbers):
    sum = 0
    average = 0
    for count in range(0, len(Numbers)):
        sum = sum + Numbers[count]
    average = sum / len(Numbers)
    print("The average of all the numbers is " + str(average))

def Multiplication(Numbers):
    product = 1
    for counter in range(0, len(Numbers)):
        product = product * Numbers[counter]
    print("The product of the numbers is " + str(product))

def SmallestNumbers(Numbers):
    SmallestNumber = Numbers[0]
    for count in range(0,len(Numbers)):
        if SmallestNumber > Numbers[count]:
            SmallestNumber = Numbers[count]
    print("The smallest number is " + str(SmallestNumber))

#
# The following code will take an input of 10 numbers and then present the sum of all those numbers.
#
print("For addition press 1")
print("For largest number press 2")
print("For squares press 3")
print("For average press 4")
print("For product press 5")
print("For smallest number press 6")
Operation = int(input("Pick an operation: "))

if Operation < 1 or Operation > 6:
    print("There are no operations for the number that you have chosen.")
    exit()

print("Type 'exit' to stop inputing numbers")

Numbers = []
for counter in range(0,10):
    NumberString = ""
    Suffix = ""
    NumberSuffix = ""
    if counter == 0:
        Suffix = "st"
    if counter == 1:
        Suffix = "nd"
    if counter == 2:
        Suffix = "rd"
    if counter > 2:
        Suffix = "th"
    NumberSuffix = str(counter + 1) + Suffix
    NumberString = input("Input the " + NumberSuffix + " number: ")
    if NumberString == "exit" or NumberString == "Exit":
        break
    Numbers.append(int(NumberString))

if Operation == 1:
    Sum(Numbers)
elif Operation == 2:
    LargestNumber(Numbers)
elif Operation == 3:
    Squares(Numbers)
elif Operation == 4:
    Average(Numbers)
elif Operation == 5:
    Multiplication(Numbers)
elif Operation == 6:
    SmallestNumbers(Numbers)