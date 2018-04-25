from math import *
import string
import random

WORDLIST_FILENAME = "D:/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n")
    return wordlist


wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

secretWord = chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    s = len(secretWord)
    for i in secretWord:
        if i in lettersGuessed:
            s -= 1
    return s == 0


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    s = ""
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            s += '_ '
        else:
            s += secretWord[i]
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    S = string.ascii_lowercase
    T = ""
    for i in range(len(S)):
        if S[i] not in lettersGuessed:
            T += S[i]
    return T

def theMan(N):
    man = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
               "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
               "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
               "_______\n|     |\n|\n|\n|\n|\n|\n=======",
               ]
    print(man[N])

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    """
    print("Welcome to the game, Hangman! ")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    i = 6
    test = True
    lettersGuessed = []
    while test:
        theMan(i)
        print("-----------")
        S = getGuessedWord(secretWord, lettersGuessed)
        print("You have", i, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        a = input("Please guess a letter:")
        if a in lettersGuessed :
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        lettersGuessed.append(a)
        T = getGuessedWord(secretWord, lettersGuessed)
        if S == T:
            print("Oops! That letter is not in my word:", S)
            i -= 1
        else:
            print("Good guess:", T)

        if T == secretWord:
            print("Congratulations, you won!")
            test = False
        elif i == 0:
            theMan(i)
            print("-----------")
            print("Sorry, you ran out of guesses. The word was else.")
            print("the word is", secretWord)
            test = False



hangman(secretWord)
