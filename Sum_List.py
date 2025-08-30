#
# The following code will take an input of 10 numbers and then present the sum of all those numbers.
#
print("For addition press 1")
print("For largest number press 2")
print("For squares press 3")
print("For average press 4")
Operation = int(input("Pick an operation: "))

Numbers = []
for counter in range(0,10):
    NumberString = ""
    NumberString = input("Input a number: ")
    Numbers.append(int(NumberString))

# End of For

sum = 0
LargestNumber = Numbers[0]
SquareList = []
average = 0

for count in range(0,10):

    # Compute sum
    if Operation == 1:
        sum = sum + Numbers[count]

    # Compute the largest number
    elif Operation == 2:
        if LargestNumber < Numbers[count]:
            LargestNumber = Numbers[count]

    # Compute the squares
    elif Operation == 3:
        SquareList.append(Numbers[count]*Numbers[count])

    # Compute the average.
    elif Operation == 4:
        sum = sum + Numbers[count]
    # End of If blocks

# End of For block

if Operation == 4:
        average = sum / len(Numbers)

# Print the answer now
if Operation == 1:
    print("The sum of the numbers is " + str(sum))
elif Operation == 2:
    print("The largest number is " + str(LargestNumber))
elif Operation == 3:
    print("The square of all the numbers are: ")
    print(SquareList)    
elif Operation == 4:
    print("The average of all the numbers is " + str(average))