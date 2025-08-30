import random
import Hangman_Art
import Hangman_Words

print(Hangman_Art.logo)

def ReplaceCharacter(string, position, newLetter):
    characters = []
    newString = ""
    for j in range(0, len(string), 2):
        characters.append(string[j])
    characters[position] = newLetter
    for _ in range(0, len(characters)):
        newString += characters[_] + " "
    return(newString)


def RepeatGuess(guessed, character):
    contains = False
    for l in range(0, len(guessed)):
        if guessed[l] == character:
            return(True)
    return(False)


complete = False
guessed = []
display = ""
lose = False
lives = 6

# Computer chooses a random word from the given word list
position = random.randint(0, len(Hangman_Words.word_list) - 1)
chosen_word = Hangman_Words.word_list[position]

# Creates the display of a hidden word and prints it
for i in range(len(chosen_word)):
    display = display + "_ "
print(display)


while complete == False:
# Takes a guess from the user
    guess = input("Guess a letter? \n").lower()
    if RepeatGuess(guessed, guess) == False:
        guessed.append(guess)
    else:
        print("You already guessed this letter", end = "\n\n")
        print(display, end = "\n\n")
        print(f"Guessed letters: {guessed}", end = "\n\n")
        print(Hangman_Art.stages[lives])
        continue
    # Checks the guess with the word and replaces each dash with the letter and prints it.
    for spot in range(0, len(chosen_word)):
        if guess == chosen_word[spot]:
            display = ReplaceCharacter(display, spot, guess)
    if guess not in chosen_word:
        lives += -1
    if "_" not in display:
        complete = True
    print(display, end = "\n\n")
    print(f"Guessed letters: {guessed}", end = "\n\n")
    print(Hangman_Art.stages[lives])
    if lives == 0:
        lose = True
        break
if lose == False:
    print("You Win!")
else:
    print("You Lose")
    print(f"The word was {chosen_word}")