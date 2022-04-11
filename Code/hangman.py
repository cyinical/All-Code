import os

name = input('What is your name:\n')
play = input('Would you like to play Hangman with me?\nY/N').upper()
if play == 'Y':
    print('oki lets play! You have 5 lives, dont lose them all!')
else:
    print('maybe next time!')
    os._exit(1)

word = "bowl"

lives = 5

guess = ''

hint = 'Something you eat out of'

asking = 1

while lives > 0:

    fail = 0

    for char in word:
        if char in guess:
            print(char)
        else:
            print('_')
            fail += 1

    if fail == 0:
        print('you won!')
        break

    print()
    guessing = input("\nHint: It's something you eat out of\nGuess a character:\n").lower()
    guess += guessing

    if guessing not in word:
        lives -= 1
        print('wrong letter\nYou have', + lives, 'lives remaining!')
        if lives == 0:
            print('you have lost')
