import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    #print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    
    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    word: string (lowercase letters)
    n: integer (HAND_SIZE)
    returns: int >= 0
    """

    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


def displayHand(hand):
    """
    Displays the letters currently in the hand.
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")      
    print()          
 
    
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    newhand = hand.copy()
    for letter in word:
        if letter in newhand:
            newhand[letter] -= 1
    return newhand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    frequencyLetters_word = getFrequencyDict(word)
    counter = 0
    if word in wordList:
        for letter in word:
            if letter in hand:
                if frequencyLetters_word[letter] <= hand[letter]:
                    counter += 1
    if counter == len(word) or word == '.':
        return True
    else:
        return False
    

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


def playHand(hand, wordList, n):
    """
      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE)
    """
    totalscore = 0 # Keep track of the total score
    while calculateHandlen(hand) > 0: # As long as there are still letters left in the hand
        print('Current hand:', end=' ')
        displayHand(hand) # Display the hand
        word = input('Type in a word consisting of the letters in your hand or a "." to indicate that you are finished:') # Ask user for input
        if word == ".": # If the input is a single period:
            break
        else:
            if not isValidWord(word, hand, wordList): # If the word is not valid:
                print('This is not a valid word:Please try again.')
            else:
                totalscore += getWordScore(word, HAND_SIZE)
                print('The score of your word is ', getWordScore(word, HAND_SIZE), 'and your total score is now ', totalscore)
                hand = updateHand(hand,word) # Update the hand
    if word == '.':
        print('Your total score is  ', totalscore)
    else:
        print('You ran out of letters. Your total score is ', totalscore)


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands. 
    """
    counter = 0
    continuetoPlay = True
    while continuetoPlay:           
        decisionGame = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if decisionGame == 'e':
            continuetoPlay = False
            continue
        if decisionGame == 'n':
            counter += 1
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)            
        elif decisionGame == 'r' and counter == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif decisionGame == 'r':
            playHand(hand, wordList, HAND_SIZE)
        else:
            print('Invalid command. Please try again.')
            

playGame(loadWords())