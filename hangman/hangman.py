import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        print('you have',lives,'you have used thses letter: ',' '.join(used_letters))

        #whta current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:',' '.join(word_list))

        user_letter = input('guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1
                print('\nyour latter,', user_letter,'is not in the word.')
        elif user_letter in used_letters:
            print('you have already used this letter.pelease try again.')

        else:
            print('invalid character.please try again.')

    #gets here when len(word_letters) ==1
    if lives == 0:
        print('you died,sorry.the word was',word)
    else:
        print('you guessed the word',word,'!!')
hangman()