# create a prog which make a message encode and decode.

import random
import string


# create a random function that gives random letters form the string

def char_random(n=3):
    word = ''.join(random.choices(string.ascii_lowercase,k=n)) # choose random 3 letter from a lowercase string(a-z)
    return word


# function for encode
def encode_word(word):
    if len(word)>=3:
        new_word=word[1:]+word[0] # remove first latter and append it at the end.

        return char_random() + new_word + char_random() # prefix + word + suffix
    else:
        word_reversed = word[::-1]
        return word_reversed


# function for decode

def decode_word(word):
    if len(word)<3:
       return word[::-1]

    else:
        remove = word[3:-3] # remove prefix and suffix

        return remove[-1] + remove[:-1] # remove last letter and add remaing letter



# encode full sentence:

def encode_message(message):
    word = message.split()
    return ' '.join(encode_word(w) for w in word)

# # decode full sentence:

def decode_message(message):
    word = message.split()
    return ' '.join(decode_word(w) for w in word)


# main function

def main():
    choice = input("Enter what you want ENCODE press 1 OR DECODE press 2: ")

    if choice == '1':
        msg = input("Enter your message: ")
        secret = encode_message(msg).lower()
        print("Your encode message is: ",secret)

    elif choice == '2':
        msg_decode = input("Enter your message: ")
        secret_decode = decode_message(msg_decode).lower()
        print("Your decode message is: ",secret_decode)

    else:
        print("Invalid statement!")

if __name__ == "__main__":
    main()
