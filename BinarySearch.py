import math
data = [-4, -1, 0, 23, 99, 102, 217, 1004]
targetNum = 102
foundIndex = 0
startIndex = 0
Iterations = 0
found = False
endIndex = len(data) - 1

while startIndex != endIndex:
    middleIndex = math.floor((endIndex - startIndex + 1) / 2 + startIndex)
    if data[middleIndex] == targetNum:
        found = True
        foundIndex = middleIndex
        break
    elif targetNum > data[middleIndex]:
        startIndex = middleIndex + 1
    else:
        endIndex = middleIndex - 1
    Iterations += 1

if data[startIndex] == targetNum:
    found = True
    foundIndex = startIndex

if found == True:
    print("The number " + str(targetNum) + ", is found at position " + str(foundIndex))
    print("It took " + str(Iterations) + " iterations to find the inputted number")
else:
    print("The number " + str(targetNum) + "is not in the given list")