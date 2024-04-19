
NUM_ALPHAS = 26

class Message:
    def __init__(self, letter1, letter2, letter3, letter4):
        self.letter1 = letter1
        self.letter2 = letter2
        self.letter3 = letter3
        self.letter4 = letter4    

# Encipher a letter by a given offset
def encipher_letter(letter, offset):
    offset = offset % NUM_ALPHAS + NUM_ALPHAS
    if letter >= 'a' and letter <= 'z':
        return chr(ord('a') + (ord(letter) - ord('a') + offset) % NUM_ALPHAS)
    else:
        return chr(ord('A') + (ord(letter) - ord('A') + offset) % NUM_ALPHAS)

# Decipher a letter by a given offset
def decipher_letter(letter, offset):
    offset = offset % NUM_ALPHAS - NUM_ALPHAS
    if letter >= 'a' and letter <= 'z':
        return chr(ord('a') + (ord(letter) - ord('a') - offset) % NUM_ALPHAS)
    else:
        return chr(ord('A') + (ord(letter) - ord('A') - offset) % NUM_ALPHAS)

# Encipher a message
def encipher(msg):
    offsets = input("Enter the numbers to encipher by: ").split()
    offsets = [int(offset) for offset in offsets]

    return encipher_letter(msg.letter1, offsets[0]) + encipher_letter(msg.letter2, offsets[1])\
    + encipher_letter(msg.letter3, offsets[2]) + encipher_letter(msg.letter4, offsets[3])

# Decipher a message
def decipher(msg):
    offsets = input("Enter the numbers to decipher by: ").split()
    offsets = [int(offset) for offset in offsets]

    return decipher_letter(msg.letter1, offsets[0]) + decipher_letter(msg.letter2, offsets[1])\
    + decipher_letter(msg.letter3, offsets[2]) + decipher_letter(msg.letter4, offsets[3])

# Determines cyphering for a given msg and prints out the result
def determine_ciphering(msg):
    cipher = input("Would you like to encipher or decipher this message (e/d)? ")
    if cipher == 'e':
        print(encipher(msg))
    elif cipher == 'd':
        print(decipher(msg))
    else: 
        print("You did not enter 'e' or 'd', now exiting...\n")

def main():
    word = input("Message: ")
    msg = Message(word[0], word[1], word[2], word[3])
    determine_ciphering(msg)


main()