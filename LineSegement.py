def Coordinates(string):
    FirstNumber = True
    FirstNum = ""
    SecondNum = ""
    i_iter = 0
    while i_iter < len(string):
        if string[i_iter] == ",": 
            FirstNumber = False
        else:
            if FirstNumber == True:
                FirstNum = FirstNum + string[i_iter]
            elif FirstNumber == False:
                SecondNum = SecondNum + string[i_iter]
        i_iter += 1
    tuple = (int(FirstNum), int(SecondNum))
    return(tuple)

def LongestLineSegment(list):
    LongestLine = list[0]
    for i_iter in range(0, len(list)):
        if abs(LongestLine[1] - LongestLine[0]) < abs(list[i_iter][1] - list[i_iter][0]):
            LongestLine = list[i_iter]
    return(LongestLine)


def ShortestLineSegment(list):
    ShortestLine = list[0]
    for i_iter in range(0, len(list)):
        if abs(ShortestLine[1] - ShortestLine[0]) > abs(list[i_iter][1] - list[i_iter][0]):
            ShortestLine = list[i_iter]
    return(ShortestLine)

def LineIntersect(list, StartLine):
    NumLines = 0
    for i_iter in range(0, len(list)):
        for j_iter in range(list[i_iter][0], abs(list[i_iter][1] - list[i_iter][0])):
            if list[i_iter][1] - list[i_iter][0] > 0:
                if list[i_iter][0] + j_iter > StartLine[0] and list[i_iter][0] + j_iter < StartLine[1]:
                    NumLines += 1
                    break 
            if list[i_iter][1] - list[i_iter][0] > 0:                    
                if list[i_iter][0] - j_iter > StartLine[0] and list[i_iter][0] - j_iter < StartLine[1]:
                    NumLines += 1
                    break
    return(NumLines)


print("Press 1 to get the longest line")
print("Press 2 to get the shortest line")
print("Press 3 to find how many times a certain line gets intersected")
Operation = int(input("Pick an operation: "))

if Operation == 3:
    StartLine = Coordinates(input("Pick a line to start: "))
list = []
while True:
    string = input("Enter coordinates for a line here: ")
    if string == "exit":
        break
    list.append((Coordinates(string)))

if Operation == 1:
    print(LongestLineSegment(list))
elif Operation == 2:
    print(ShortestLineSegment(list))
elif Operation == 3:
    print(LineIntersect(list, StartLine))