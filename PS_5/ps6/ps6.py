import string


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    '''
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift.
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet(0 <= shift < 26)

        Returns: a dictionary mapping a letter (string) to 
        another letter (string). 
        '''
        self.encrypting_dict = {}
        for i in range(len(string.ascii_lowercase)):
            letter = string.ascii_lowercase[i]
            capitalLetter = string.ascii_uppercase[i]
            if i + shift >= len(string.ascii_lowercase):
                index = i + shift - len(string.ascii_lowercase)
            else:
                index = i + shift
            self.encrypting_dict[letter] = self.encrypting_dict.get(letter,'') + string.ascii_lowercase[index]
            self.encrypting_dict[capitalLetter] =self.encrypting_dict.get(capitalLetter,'') + string.ascii_uppercase[index]
        return self.encrypting_dict
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
        down the alphabet by the input shift
        '''
        self.message_text_encrypted = ''
        for letter in self.message_text:
            if letter.lower() in string.ascii_lowercase: 
                self.message_text_encrypted += self.build_shift_dict(shift)[letter]
            else:
                self.message_text_encrypted += letter
        return self.message_text_encrypted



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self,text)
        Message.build_shift_dict(self,shift)
        Message.apply_shift(self,shift)
        self.shift = shift
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shift = shift_counter = validWords = validWords_counter = 0
        while shift_counter <= 25:
            decrypted_message_text = self.apply_shift(26 - shift_counter)
            decrypted_message_list = decrypted_message_text.split(' ')
            for word in decrypted_message_list:
                if is_word(self.valid_words, word):
                    validWords_counter += 1
            if validWords_counter > validWords:
                validWords = validWords_counter
                shift = shift_counter
            shift_counter += 1
        decryptedMessage = self.apply_shift(26 - shift)
        return (26 - shift, decryptedMessage)



#test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
    
#test case (CiphertextMessage)
#ciphertext = CiphertextMessage('jgnnq')
#print('Expected Output:', (24, 'hello'))
#print('Actual Output:', ciphertext.decrypt_message())
        
    
def decrypt_story():
    encrypted_story = get_story_string()
    decrypted_story= CiphertextMessage(encrypted_story)
    return decrypted_story.decrypt_message()


print(decrypt_story())