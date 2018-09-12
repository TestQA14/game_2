# -*- coding: utf-8 -*-
import random

MAX_ERRORS = 8

word_list = ['raw', 'oil', 'car', 'plain', 'library', 'ball', 'olimpic', 'victory', \
             'game', 'loosing']

secret_word = random.sample(word_list, 1)[0]
print(secret_word)


def print_list_as_string(arg):
    print(''.join(users_word))


users_word = ['*'] * len(secret_word)
errors_counter = 0

while True:
    letter = raw_input('Input letter in word: ').lower()
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for pos, char in enumerate(secret_word):
            if char == letter:
                users_word[pos] = letter
        if '*' not in users_word:
            print('You win!!!')
            print_list_as_string(users_word)
            break
    else:
        errors_counter += 1
        print('Errors: ', errors_counter)

        if errors_counter == MAX_ERRORS:
            print('You are lost :(')
            break

    print_list_as_string(users_word)
