import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
   # print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
            
    if counter == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    partialWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            partialWord += letter
        else:
            partialWord += ' _ '
    
    return partialWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    possibleGuesses = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            possibleGuesses += letter
    
    return possibleGuesses


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    '''
    
    lettersGuessed = []
    guesses = 1
    
    print('Welcome to the game Hangman!', '\nI am thinking of a word that is', len(secretWord), 'letters long.', '\n-------------')
    #print(secretWord)
    
    while guesses <= 8 and not isWordGuessed(secretWord, lettersGuessed):
        print('You have' , 9 - guesses, ' guesses left.', '\nAvailable letters:',getAvailableLetters(lettersGuessed))
        letterGuessed = input('Please guess a letter:')
        if letterGuessed in lettersGuessed:
            print('You have already guessed that letter:', getGuessedWord(secretWord, lettersGuessed), '\n------------' )
            continue
        
        lettersGuessed.append(letterGuessed)
        
        if letterGuessed in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed), '\n------------')
        else:
            print('That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed), '\n------------')
            guesses += 1
        
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('You ran out of guesses. The word was ' + secretWord + '.')


hangman(chooseWord(loadWords()).lower())