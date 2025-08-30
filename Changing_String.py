def ReverseString(string):
    BackwordsString = ""
    list = []
    for counter in range(0, len(string)):
        list.append(string[counter])
    for counter in range(0, len(string)):
        BackwordsString = BackwordsString + (list[len(string) - (counter + 1)])
    print(BackwordsString)

def Pallendrome(string):
    for counter in range(0, int(len(string) / 2)):
        if string[counter] != string[len(string) - (counter + 1)]:
            print("The string is not a pallendrome.")
            exit()
    print("The string is a pallendrome")

def FirstCharacter(string):
    Unique = False
    for i_iter in range(0, len(string)):
        Occur = 0
        Character = string[i_iter]
        for j_iter in range(0, len(string)):
            if Character == string[j_iter]:
                Occur += 1
        if Occur == 1:
            Unique = True
            break        
    # End of outer for loop
    if Unique == True:
        return(Character)
    else:
        return("There is no unique letter")
# End of def

def FirstCharacter_1(string):

    Unique_char = "There is no unique letter"
    for i_iter in range(0, len(string)):
        Occur = 0
        Character = string[i_iter]
        for j_iter in range(0, len(string)):
            if Character == string[j_iter]:
                Occur += 1
        if Occur == 1:
            Unique_char = Character
            break        
    # End of outer for loop

    return(Unique_char)

#
# The function below uses a dictionary to find out the first unique character in the list
#
def DictFirstCharacter(string):
    dict = {}
    list = []
    UniqueCharacter = "There is no unique character"

    # Insert items from string to a list 
    for i_iter in range(0, len(string)):
        list.append(string[i_iter])
    # End of for

    # Insert elements from list to a dictionary
    for j_iter in range(0, len(list)):
        if list[j_iter] in dict:
            value = dict[list[j_iter]]
            value += 1
            dict[list[j_iter]] = value
        else:
            dict[list[j_iter]] = 1
    #End of for

    # Uses dictrionary to find the first unique letter
    for counter in range(0, len(list)):
        if dict[list[counter]] == 1:
            UniqueCharacter = list[counter]
            break
    # End of for
                
    return(UniqueCharacter)
# End of function



# End of def

print("Press 1 for a string reversed")
print("Press 2 to find if the string is a pallendrome")
print("Press 3 to find the first character of the string")
Operation = int(input("Pick an operation: "))
string = str(input("Input a string here: "))

if Operation == 1:
    ReverseString(string)
elif Operation == 2:
    Pallendrome(string)
elif Operation == 3:
    print(DictFirstCharacter(string))