"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def play_game(secret_word):
    """
    This function handles the user interaction component of the game.
    It chooses a random word from a word list to use as the secret word,
    asks the user to guess a letter, keeps track of the user’s partially
    guessed word and the number of guesses remaining, prints out the various
    messages, detects the end of the game, and so forth.
    """
    is_end = False
    guessed_word = '-' * len(secret_word)
    num_guesses = INITIAL_GUESSES
    idx_list = []
    while not is_end:
        print(f'The word now looks like this: {guessed_word}')
        print(f'You have {num_guesses} guesses left')
        letter = input('Type a single letter here, then press enter: ')
        if len(letter) > 1:
            print('Guess should only be a single character.')
            continue
        else:
            letter = letter.upper()
            if letter in secret_word:
                print('That guess is correct.')
                idx_list = find_all(secret_word, letter)
                for idx in idx_list:
                    guessed_word = guessed_word[:idx] + secret_word[idx] + guessed_word[idx + 1:]
            else:
                print(f"There are no {letter}'s in the word")
                num_guesses -= 1
            if num_guesses == 0:
                is_end = True
                print(f'Sorry, you lost. The secret word was: {secret_word}')
            if '-' not in guessed_word:
                print(f'Congratulations, the word is: {secret_word}')
                is_end = True


def find_all(str, letter):
    """
    This function is passed a string and a letter and returns a list of indices
    showing the position of the letter in the string.
    >>> find_all('HAPPY', 'P')
    [2, 3]
    """
    idx_list = []
    idx = 0
    while True:
        idx = str.find(letter, idx)
        if idx != -1:
            idx_list.append(idx)
            idx += 1
        else:
            return idx_list


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    word_list = []
    with open(LEXICON_FILE) as file:
        for line in file:
            line = line[:-1]
            word_list.append(line)
    index = random.randrange(len(word_list))
    return word_list[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
