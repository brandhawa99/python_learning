import json
import random


def getWord():
    try:
        with open("words.json") as words_file:
            words = words_file.read()
            data = json.loads(words)
            words_list = data["data"]
            word = words_list[int(len(words_list) * random.random())]
            return word
    except:
        print("Could not get word")


def createGame():
    GUESSES = 7
    word = getWord()
    split_word = [*word]
    guessed_letters = []
    i = 0
    while i < GUESSES:
        guessed_letters.append(input("Enter a Letter: "))
        print("Guessed Letters", guessed_letters)
        data = printBoard(guessed_letters, split_word)
        if not data["contains"]:
            i += 1
        if "_" not in data["string"]:
            print("YOU GOT THE WORD")
            break
    print(f"THE WORD WAS {word}")


def printBoard(guess, word):
    string = ""
    contains = False
    for x in range(len(word)):
        if word[x] in guess:
            string += word[x]
            contains = True
        else:
            string += " _ "
    print(string)
    return {"contains": contains, "string": string}


createGame()
