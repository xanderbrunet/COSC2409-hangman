'''
File: COSC2409_XanderBrunet_HangmanWithFunctions.py
Name: Xander Brunet
Requirements: Create a hangman game
Constants: /
Variables: word_list, word_by_letter, invisible_word, tried_letters, tries
input: guess
calculated: tries
Output: welcome screen, game board, end of game
Key calculations: tries -= 1
Key design considerations: Have the game in a screen format that updates as the game goes on
Test data: Valid inputs, invalid inputs, winning, losing
'''

import time
import os

word_list = [
    "apple", "banana", "cherry", "dog", "elephant", "fish", "grape", "horse", "ice", "jelly", 
    "kiwi", "lemon", "mango", "nut", "orange", "pear", "quail", "rabbit", "snake", "tiger", 
    "umbrella", "violet", "water", "xylophone", "yak", "zebra", "ant", "bird", "cat", "duck", 
    "egg", "frog", "goat", "hat", "ink", "jacket", "kite", "lion", "mouse", "nest", "ostrich", 
    "penguin", "queen", "rose", "sun", "tree", "unicorn", "vase", "whale", "yacht", "zeppelin"
]
word_by_letter = []
invisible_word = []
tried_letters = []
tries = 6

def game():
    # Function to prepare the game
    def prep_game():
        import random
        random_word = random.sample(word_list, 1)
        invisible_word.clear()
        tried_letters.clear()
        word_by_letter.clear()
        global tries
        tries = 6
        for letter in random_word[0]:
            invisible_word.append("_")
        for letter in random_word[0]:
            word_by_letter.append(letter)
        return random_word[0]

    # Function to print the game board
    def print_game():
        for underscore in invisible_word:
            print(underscore, sep=' ', end=" ")
        print("\n")
        print("Tries left:", tries)
        print("Tried letters: ", end=" ")
        for letter in tried_letters:
            print(letter, end=" ")
        print("\n")

    # Function to check if the input is valid
    def check_input(guess):
        if guess.isalpha() == False:
            os.system('cls' if os.name == 'nt' else 'clear')        
            print("Please enter a letter")
            return False
        if len(guess) > 1:
            os.system('cls' if os.name == 'nt' else 'clear')        
            print("Please enter only one letter")
            return False
        if guess in tried_letters:
            os.system('cls' if os.name == 'nt' else 'clear')        
            print("You already tried that letter")
            return False
        return True

    # Function to decide what to do with the input
    def process_input(guess):
        if guess in word_by_letter and guess not in invisible_word and guess not in tried_letters:
            tried_letters.append(guess)
            for i in range(len(word_by_letter)):
                if guess == word_by_letter[i]:
                    invisible_word[i] = guess
            os.system('cls' if os.name == 'nt' else 'clear')        
            return True
        else:
            tried_letters.append(guess)
            global tries
            tries -= 1
            os.system('cls' if os.name == 'nt' else 'clear')        
            return False

    # Welcome Screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Hangman!")
    print("The word has", len(prep_game()), "letters...")
    time.sleep(2)
    print("Let's play!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Logic for the game
    # With functions, the code for the logic went from 37 lines to 5 lines
    while invisible_word != word_by_letter and tries > 0:
        print_game()
        guess = input("Guess a letter: ")
        if check_input(guess) == True:
            process_input(guess)

    # End of game
    if tries == 0:
        print("You lost! The word was: ", end="")
        for letter in word_by_letter:
            print(letter, end=" ")
        print("\n")
    else:
        print("You won!")
        print("The word was: ", end="")
        for letter in word_by_letter:
            print(letter, end=" ")
        print("\n")

    print("Play again? (y/n)")
    play_again = input()
    if play_again == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        game()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
        time.sleep(2)

game()