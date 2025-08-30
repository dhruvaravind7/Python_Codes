import Caesar_Art

def restartCode():
    restart = input("Type yes if you want to try again. Otherwise type no. \n").lower().strip()
    if restart == "yes":
        return(True)
    else:
        return(False)

def caesar(text, shift, option):
        newText = ""
        for i in range(0, len(text)):
            isNum = False
            if text[i] not in alphabet:
                isNum = True
            for j in range(0, 26):
                if isNum == True:
                    newText = newText + text[i]
                    break
                if text[i] == alphabet[j]:
                    if option == True:
                        newPos = j + shift
                        break
                    else:
                        newPos = j - shift
                        break
            if isNum == False:
                newLetter = alphabet[newPos%26]
                newText = newText + newLetter
        return(newText)

print(Caesar_Art.logo)

tryAgain = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while tryAgain == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    if direction == "encode":
        print(caesar(text, shift, True))
    elif direction == "decode":
        print(caesar(text, shift, False))
    else:
        print("Please type decode encode or decode.")
    
    tryAgain = restartCode()