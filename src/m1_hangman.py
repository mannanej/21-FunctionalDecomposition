"""
Hangman.

Authors: Eddie Mannan and Kent Smith.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random
import sys

with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()


def main():
    letter_in_word()


def get_min_length():
    min_length = int(input('Input a minimum word length.'))
    return min_length


def get_word():
    min_length = get_min_length()
    while True:
        r = random.randrange(0, len(words))
        if len(words[r]) >= min_length:
            word = words[r]
            return word


def get_num_of_guesses():
    x = int(input('How many unsuccessful guesses do you want?'))
    return x


def play_again():
    x = input('Would you like to play again? (y/n)')
    if x == 'y':
        letter_in_word()
    elif x == 'n':
        sys.exit()
    else:
        play_again()


def get_guess():
    x = input('Guess a lowercase letter.')
    return x


def letter_in_word():
    guesses = get_num_of_guesses()
    word = get_word()
    w = []
    for k in range(len(word)):
        w.append('-')
    for k in range(len(word)):
        print('-', end='')
    print()
    while True:
        guess = get_guess()
        s = []
        for k in range(len(word)):
            if word[k] == guess:
                s.append(k)
            else:
                s.append(-1)
        total = 0
        for k in range(len(s)):
            if s[k] != -1:
                total += 1
        if total == 0:
            print('Your guess was unsuccessful.')
            guesses -= 1
            print('You have', guesses, 'guesses left.')
        if guesses == 0:
            print('You lose! The secret word was:', word)
            play_again()
        for k in range(len(word)):
            if k == s[k]:
                w[k] = guess
            if w[k] is not '-':
                w[k] = w[k]
            else:
                w[k] = '-'
        for k in range(len(word)):
            print(w[k], end='')
        print()
        total = 0
        for k in range(len(word)):
            if w[k] == '-':
                total += 1
        if total == 0:
            print('You won!')
            play_again()


main()

