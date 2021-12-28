# Import random module
import random

#Import different options list from modules
from hangman_easy import words_easy
from hangman_hard import words_hard
from hangman_intermediate import words_intermediate
from hangman_pics import HANGMANPICS

#define variables
counter = 0
chances = 6
another_game = "Y"

#Loop for repeat game options
while (another_game == "Y" or another_game == "y"):
    #Presentation of options
    print("\033[1;32;40mWelcome to our music based hangman game")
    print("\033[1;37;40mRules:")
    print("\033[1;31;40m1.Choose between 3 difficulty options")
    print("2.Guess the word or sentence")
    print("Enter a space when expected")
    print("\033[1;33;40mIf you fail you have 6 opportunities to resolve the game")

    #Gamer data
    name = input("\033[1;37;40minsert player name ")
    difficulty = int(input("insert difficulty option "))

    #Difficulty options
    print("let´s start", name)
    if(difficulty < 1 or difficulty > 3):
        print("input a number between 1 and 3")
        difficulty = int(input("insert difficulty option "))
    if(difficulty == 1):
        word = random.choice(words_easy)

        print("Music types")
    if(difficulty == 2):
        word = random.choice(words_intermediate)
        print("Artists")
    if(difficulty == 3):
        word = random.choice(words_hard)
        print("Songs")

    #Start of game
    guessed_word = "_" * len(word)
    print(guessed_word)

    #Game loop
    while (guessed_word != word) and (chances):
        check_word = guessed_word
        char = input("Enter a char ")
        if (len(char) != 1):
            print("\033[1;31;40mEnter just 1 character")
            print("\033[1;37;40m")
            continue
        for letter in word:
            if (char.lower() == letter or char.upper() == letter):
                guessed_word = guessed_word[:counter] + \
                    letter[0] + guessed_word[counter + 1:]
            counter += 1
        if (check_word == guessed_word):
            chances -= 1
            print("\033[1;31;40mWrong, {} is not in the word. You have {} chances left.".format(
            char, chances))
            #Hangman images
            if (chances == 6):
                print(HANGMANPICS[0])
            if (chances == 5):
                print(HANGMANPICS[1])
            if (chances == 4):
                print(HANGMANPICS[2])
            if (chances == 3):
                print(HANGMANPICS[3])
            if (chances == 2):
                print(HANGMANPICS[4])
            if (chances == 1):
                print(HANGMANPICS[5])
            if (chances == 0):
                print(HANGMANPICS[6])
              
            print("\033[1;37;40m")
        print(guessed_word)
        counter = 0
    #Win or lose conditionals
    if (guessed_word == word):
        print("\033[1;32;40mCongrats, you have guessed the word!", name)
    else:
        print("\033[1;31;40mSorry, you've been hanged out")

    another_game = input("\033[1;37;40mDo you want to play more? Y/N ")

    if (another_game == "n" or another_game == "N"):
        exit
