import random
import numpy


class ArrayCalc:
    numbers = []
    def generateArray(self, length, ranges):
        newList = []
        for x in range(0, length):
            newList.append(random.randrange(0, ranges + 1))
        return(newList)

    def setArray(self, length, ranges):
        self.numbers = self.generateArray(length, ranges)

    def printArray(self):
        print(self.numbers)

    def findRange(self):
        maxNum = self.numbers[0]
        minNum = self.numbers[0]
        for x in range( len(self.numbers)):
            if self.numbers[x] > maxNum:
                maxNum = self.numbers[x]
            elif self.numbers[x] < minNum:
                minNum = self.numbers[x]
        return(maxNum-minNum)

    def FindMedian(self):
        if len(self.numbers) % 2 == 1:
            pos = (int) (len(self.numbers) / 2)
            median = self.numbers[pos]
        else: 
            num1 = self.numbers[(int) (len(self.numbers) / 2 - 1)]
            num2 = self.numbers[(int) (len(self.numbers) / 2)]
            median = (num1 + num2)/2
        return(median)

    def generate2DArray(self, row, col):
        linkarray = numpy.zeros(row, col)



array = ArrayCalc()
array.setArray(3, 10)
array.printArray()
print(array.findRange())
print(array.FindMedian())