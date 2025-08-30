# The function below converts the string coordinate into a tuple.
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

def GetVector(Coordinate1, Coordinate2):
    x1 = Coordinate1[0]
    y1 = Coordinate1[1]
    x2 = Coordinate2[0]
    y2 = Coordinate2[1]
    Vector = (x2-x1, y2-y1)
    return(Vector)

def GetCrossProduct(Vector1, Vector2):
    return(Vector1[0] * Vector2[1] - Vector1[1] * Vector2[0])

def DoesLineIntersect(list):
    if list[0] < 0 and list[1] > 0 and list[2] > 0 and list[3] < 0:
        return(True)
    elif list[0] < 0 and list[1] > 0 and list[2] < 0 and list[3] > 0:
        return(True)
    elif list[0] > 0 and list[1] < 0 and list[2] > 0 and list[3] < 0:
        return(True)
    elif list[0] > 0 and list[1] < 0 and list[2] < 0 and list[3] > 0: 
        return(True)
    else:
        return(False)

Coordinate1 = StringToCoordinates(input("Enter your first coordinate for your first line here: "))
Coordinate2 = StringToCoordinates(input("Enter your second coordinate for your first line here: "))
Coordinate3 = StringToCoordinates(input("Enter your first coordinate for your second line here: "))
Coordinate4 = StringToCoordinates(input("Enter your second coordinate for your second line here: "))

list = []

list.append(GetCrossProduct(GetVector(Coordinate1, Coordinate3), GetVector(Coordinate4, Coordinate3)))
list.append(GetCrossProduct(GetVector(Coordinate2, Coordinate3), GetVector(Coordinate4, Coordinate3)))
list.append(GetCrossProduct(GetVector(Coordinate3, Coordinate1), GetVector(Coordinate2, Coordinate1)))
list.append(GetCrossProduct(GetVector(Coordinate4, Coordinate1), GetVector(Coordinate2, Coordinate1)))

if DoesLineIntersect(list) == True:
    print("The two lines intersect")
else:
    print("The two lines do not intersect")