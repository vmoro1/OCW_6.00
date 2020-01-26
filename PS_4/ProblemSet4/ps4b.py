from ps4a import *
import time


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.
    This word should be calculated by considering all the words
    in the wordList.
    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestScore = 0
    bestWord = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if (score > bestScore):
                bestScore = score
                bestWord = word
    return bestWord


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    totalScore = 0
    while (calculateHandlen(hand) > 0) :
        print("Current Hand: ", end=' ')
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        else:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            else: 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                hand = updateHand(hand, word)
                print()
    print('Total score: ' + str(totalScore) + ' points.')


def playGame(wordList):
    """
    Allow the user/computer to play an arbitrary number of hands.

    wordList: list (string)
    """

    counter = 0
    hand = dealHand(HAND_SIZE)
    continuetoPlay = True
    while continuetoPlay:           
        decisionGame = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if decisionGame == 'e':
            continuetoPlay = False
            continue
        if decisionGame == 'n':
            hand = dealHand(HAND_SIZE)
        computer_orUser = input('Enter u to have yourself play and c to have the computer play:')
        if computer_orUser == 'u':
            playoneHand = playHand(hand, loadWords(), HAND_SIZE)
        else:
            playoneHand = compPlayHand(hand,loadWords(), HAND_SIZE)                
        if decisionGame == 'n':
            counter += 1
            playoneHand      
        elif decisionGame == 'r' and counter == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif decisionGame == 'r':
            playoneHand
        else:
            print('Invalid command. Please try again.')


def playGameImproved(wordList, hand=None, ans=None):
    while ans != 'e':
        player = ans = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if ans == 'n' or (ans == 'r' and hand != None):
            hand = hand if ans == 'r' else dealHand(HAND_SIZE)
            while player not in 'uc':
                player = input('Enter u to have yourself play, c to have the computer play: ')
                playHand(hand, wordList, HAND_SIZE) if player == 'u' else \
                compPlayHand(hand, wordList, HAND_SIZE) if player == 'c' else print('Invalid command.')
        elif ans == 'r':
            print('You have not played a hand yet. Please play a new hand first!')
        elif ans != 'e':
            print('Invalid command.')
            
            
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)