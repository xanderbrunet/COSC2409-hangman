# Hangman Game Documentation (COSC2409_XanderBrunet_HangmanWithFunctions.py)

**Author:** Xander Brunet

## Overview

This Python project implements a classic Hangman game with a focus on code organization through functions. 

## Requirements

* Create a functional Hangman game.

## Variables

* **`word_list`:** A list of potential words for the game.
* **`word_by_letter`:**  Stores the selected word as a list of individual letters.
* **`invisible_word`:**  Represents the player's progress, initially filled with underscores.
* **`tried_letters`:**  Keeps track of the player's previous guesses.
* **`tries`:** The number of remaining guesses (starts at 6).

## Key Design Considerations

* User-friendly interface with the game board updating after each turn.

## Functions

### `game()`

* The main game function. Handles game setup, win/loss conditions, and the option to play again.
* **Sub-functions:**
    * **`prep_game()`** 
        * Selects a random word.
        * Initializes game variables (`word_by_letter`, `invisible_word`, `tried_letters`, `tries`).
    * **`print_game()`**
        * Displays the game board (word progress, remaining tries, tried letters).
    * **`check_input(guess)`**
        * Validates the player's guess:
            * Must be a single letter.
            * Must not have been guessed previously.
    * **`process_input(guess)`**
        * Updates `invisible_word` if the guess is correct.
        * Updates `tried_letters` and decrements `tries` if the guess is wrong.

## Game Flow

1. **Welcome Screen**
2. **Game Setup** (`prep_game()` is called)
3. **Game Loop**
    * Player views the game board (`print_game()`).
    * Player enters a guess.
    * Input is validated (`check_input()`).
    * Game state is updated (`process_input()`).
    * Loop continues until the player wins or loses.
4. **End of Game** (Displays the outcome and the correct word)
5. **Play Again?** (Prompts the user; calls `game()` if yes)

## Testing

Consider testing the game with the following inputs:

* Valid single letters.
* Invalid inputs (numbers, symbols, multiple characters).
* Winning scenarios.
* Losing scenarios. 
