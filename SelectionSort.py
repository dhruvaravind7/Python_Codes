counter = 0
data = [1,3,0,8,6,2,9,5]
i = 0
j = 1

while i < len(data):
    smallestNumber = data[i]
    smallestNumIndex = i
    while j < len(data):
        if data[smallestNumIndex] > data[j]:
            smallestNumber = data[j]
            smallestNumIndex = j
        j = j + 1
    holding = data[i]
    data[i] = smallestNumber
    data[smallestNumIndex] = holding
    i = i + 1
    j = i  

print(data)