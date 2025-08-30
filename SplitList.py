def splitList(numList, splitNum): 
    counter = 0
    startLock = 0
    endLock = 0
    while counter < len(numList):
        if numList[startLock] > splitNum:
            holding = numList[startLock]
            numList[startLock] = numList[len(numList) - 1 - endLock]
            numList[len(numList) - 1 - endLock] = holding
            endLock += 1
        else:
            startLock += 1

        counter += 1

    return(numList)

list1 = [1, 3, 7, 9, 5, 2, 8]
list2 = [0, 0, 0, 0, 0, 0, 0]
list3 = [-3, 4, 6, 2, -1, -3, 0]
list4 = [6, 7, 8, 9, 13, 31, 12]

print(splitList(list1, 5))
print(splitList(list2, -2))
print(splitList(list3, 3))
print(splitList(list4, 3))