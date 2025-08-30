def StringToCoordinates(string):    
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

def LineSegmentToVector(Coordinate1, Coordinate2):
    x1 = Coordinate1[0]
    y1 = Coordinate1[1]
    x2 = Coordinate2[0]
    y2 = Coordinate2[1]
    Vector = (x2-x1, y2-y1)
    return(Vector)

def VectorCrossProduct(Vector1, Vector2):
    return(Vector1[0] * Vector2[1] - Vector1[1] * Vector2[0])

def IsCoordinateClockwise(CrossProuct):
    if CrossProuct > 0:
        return(True)
    else:
        return(False)    

Coordinate1 = StringToCoordinates(input("Input a coordinate here: "))
Coordinate2 = StringToCoordinates(input("Input a coordinate here: "))
Coordinate3 = StringToCoordinates(input("Input a coordinate here: "))
list = []

list.append(LineSegmentToVector(Coordinate1, Coordinate2))
list.append(LineSegmentToVector(Coordinate1, Coordinate3))

if IsCoordinateClockwise(VectorCrossProduct(list[0], list[1])) == True:
    print("The line turns counterclockwise")
else:
    print("The line turns clockwise")