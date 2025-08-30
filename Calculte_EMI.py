import turtle

import tkinter

# The function below nullfies the "%" in the interest input.
def PercentToNumber(string):
    NewNum = ""
    for iter in range(0, len(string)):
        if string[iter] == "%":
            break
        else:
            NewNum = NewNum + string[iter]
    return(float(NewNum))


# The function below converts the inputed string into a number.
def StringToNumber(string):
    NewNumber = ""
    for iter in range(0, len(string)):
        if string[iter] != ",":
            NewNumber = NewNumber + string[iter]
    return(int(NewNumber))

# The function adds commas after every 3rd digit.
def NumberWithComma(number):
    iter = 0
    number = str(number)
    NewNumber = ""
    while iter < len(number):
        if iter != 0 and iter % 3 == 0:
            NewNumber = "," + NewNumber
        NewNumber = number[len(number) - (1 + iter)] + NewNumber
        iter += 1
    return(NewNumber)

# The function calculates the EMI given the Principle, Interest Rate, and Time
def CalculateEMI(P, R, N):
    EMI = 0
    EMI = (P*(R/12)) * ((1+(R/12))**N) / ((1+(R/12))**N-1)
    return(float(EMI)) 

# The function calculates the interest that is being payed for a specific month. 
def CalculateMonthlyInterest(Principle, Interest):
    return(float(Principle * Interest/12))

# The function calculates the principle that is being payed for a specific month.
def CalculateMonthlyPrinciple(EMI, MonthlyInterest):
    return(EMI - MonthlyInterest)

# This function draws the entire graph in the turltle graphics window.
def DrawEMIGraph(EMI, PrincipleList, InterestList, Time, MonthInterest, MonthPrinciple, Month):
    iter = 0
    i_iter = 0
    j_iter = 10000  
    YearNum = 0
    t = turtle.Pen()
    ScaleFactor = EMI / 300
    MonthDistance = 1450 / Time
    t.up()
    t.goto(-100,EMI/ScaleFactor + 70)
    t.write("EMI Distribution", font = ("Times", 40, "bold"))
    t.speed(100)
    t.goto(0,0)
    t.backward(710)
    t.down()

# The loop below is used for creating the box where the graph is going to be added.    
    while i_iter < 2: 
        t.forward(1450)
        t.left(90)
        t.forward(int(EMI/ScaleFactor))
        t.left(90)  
        i_iter += 1
        

# The loop below draws the units on the left side of the graph.   
    while j_iter <= EMI:
        t.up()
        t.goto(-740, j_iter / ScaleFactor)
        t.write(str(int(j_iter/1000)) + "K", font = ("Times", 10, "bold"))
        j_iter += 10000

    t.goto(-710,0)
    t.heading()
    t.left(90)

    # This while loop is used for drawing all of the bars in the graph.
    while iter < len(InterestList):
        t.forward(InterestList[iter] / ScaleFactor)
        
        # This if statement is used to draw the red line for the month that was chosen.       
        if iter == Month + 1:
            t.pencolor("red")
            t.forward(PrincipleList[iter] / ScaleFactor)
            t.pencolor("blue")
        else: 
            t.pencolor("blue")
            t.forward(PrincipleList[iter] / ScaleFactor)
            
        # The code below is meant to draw the bar for each month.    
        t.right(90)
        t.forward(MonthDistance)
        t.right(90)
        t.forward(PrincipleList[iter] / ScaleFactor)
        t.pencolor("black")
        t.right(90)
        t.forward(MonthDistance)
        t.backward(MonthDistance)
        t.left(90)
        t.forward(InterestList[iter] / ScaleFactor)
        
        # This if statement is used for drawing the units at the bottom of the graph.
        if iter % 12 == 0:
            t.up()
            t.forward(25)
            t.right(90)
            t.forward(int(MonthDistance / 2))
            t.right(90)
            t.down()
            t.forward(25)
            t.backward(25)
            t.left(90)
            t.up()
            t.forward(int(MonthDistance / 2))

            # This is meant to write what year it is on the graph
            if iter == 0:
                t.write("Start", font = ("Times", 15, "bold"))
            else:
                t.write("Year " + str(YearNum), font = ("Times", 15, "bold"))
            t.backward(MonthDistance)
            t.left(90)
            t.backward(25)
            t.down()
            YearNum += 1
        t.right(180)

        # This function is used to draw the same bar except in red for the month that the user chose.
        if iter == Month:
            t.pencolor("red")
            t.left(90)
            t.forward(MonthDistance)
            t.right(90)
            t.forward(InterestList[iter] / ScaleFactor)
            t.forward(PrincipleList[iter] / ScaleFactor)
            t.right(90)
            t.forward(MonthDistance)
            t.right(90)
            t.forward(PrincipleList[iter] / ScaleFactor)
            t.forward(InterestList[iter] / ScaleFactor)
            t.right(180)
            t.up()
            t.backward(25)
            t.left(90)
            t.forward(MonthDistance/2)
            t.right(90)
            t.down()
            t.forward(25)
            t.backward(25)
            t.left(90)
            t.up()
            t.forward(MonthDistance/2)
            t.write(str(Month), font = ("Times", 15, "bold"))
            t.backward(MonthDistance)
            t.right(90)
            t.forward(25)
            t.down()
        iter += 1
        # End of while

    # This code is meant to write all of the information at the bottom of the graph.        
    t.up()
    t.goto(-710,0)
    t.write("Interest", font = ("Times", 40, "bold"))
    t.goto(-710, int((EMI / ScaleFactor) - 50))
    t.write("Principle", font = ("Times", 40, "bold"))
    t.goto(-200,-100)
    t.write("Total Money spent: $" + str(NumberWithComma(round(float(EMI * Time)))), font = ("Times", 30, "bold"))
    t.goto(-200, -150)
    t.write("EMI: $" + str(NumberWithComma(round(float(EMI)))), font = ("Times", 30, "bold"))
    t.goto(-200,-200)
    t.write("Principle for month " + str(Month) + ": $" + str(NumberWithComma(round(float(MonthPrinciple)))), font = ("Times", 30, "bold"))
    t.goto(-200,-250)
    t.write("Interest for month " + str(Month) + ": $" +  str(NumberWithComma(round(float(MonthInterest)))), font = ("Times", 30, "bold"))
    t.hideturtle()

# This piece of code was meant to take all the inputs the user gave.
Principle = StringToNumber(input("Input the total amount loaned: "))
OriginalPrinciple = Principle
Interest = float(PercentToNumber(input("Input the interest : ")) / 100)
Time = StringToNumber(input("Input the duration of the loan in months: "))
Month = int(input("Enter which month you want to get the calculations for: "))
EMI = CalculateEMI(Principle, Interest, Time)
InterestList = []
PrincipleList = []

# The function below is used to add the Monthly Interest and Principle to their respective lists.
for iter in range(0, int(Time)):
    MonthlyInterest = CalculateMonthlyInterest(Principle, Interest)
    InterestList.append(MonthlyInterest)
    MonthlyPrinciple =  CalculateMonthlyPrinciple(EMI, MonthlyInterest)
    PrincipleList.append(MonthlyPrinciple)
    Principle = Principle - MonthlyPrinciple

# This code prints some of the information that was calculated and calls the DrawEMIGraph function
print("The EMI is " + str(int(EMI)))
print("The interest for month " + str(Month) + " is " + str(int(InterestList[Month - 1])))
print("The principle for month " + str(Month) + " is " + str(int(PrincipleList[Month - 1])))
MonthInterest = str(InterestList[Month - 1])
MonthPrinciple = str(PrincipleList[Month - 1])
DrawEMIGraph(EMI, PrincipleList, InterestList, Time, MonthInterest, MonthPrinciple  , Month)

# This code is used to write the information that the user inputed 
t = turtle.Pen()
t.up()
t.goto(-710,-150)
t.write("Loan Amount: $" + str(NumberWithComma(OriginalPrinciple)), font = ("Times", 30, "bold"))
t.goto(-710,-200)
t.write("Loan Interest: " + str(round((Interest * 100),1)) + "%", font = ("Times", 30, "bold"))
t.goto(-710,-250)
t.write("Loan Duration: " + str(int(Time)) + " months", font = ("Times", 30, "bold"))
t.hideturtle()
tkinter.mainloop()