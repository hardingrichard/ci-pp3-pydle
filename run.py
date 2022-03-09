"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 5 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""

from typing import List
import random
from colorama import Fore  # Library for changing terminal text colour
from character_rule import CharacterRule
from pydle_logic import Pydle

# Pydle interface functions


def username():
    """
    Function to create the player username for greeting
    """
    # Possibly add a log in prompt here for username and password.
    user = input("To begin playing please enter Your Username: ").capitalize()
    print("\nWelcome to Pydle " + Fore.MAGENTA + f"{user}! " + Fore.RESET +
          "This is a Python CLI version of the \n"
          "popular game Wordle. In this version you will have 5 attempts \n"
          "at guessing the hidden word. To add an extra challenge, the \n"
          )
    print("word you will be guessing is 7 letters long..." + Fore.GREEN +
          " Good luck!\n" + Fore.RESET
          )


def main():  # main function placeholder
    username()
    pydle = Pydle("JACUZZI")

    while pydle.guess_still:
        # convert user input to uppercase to match against hidden word.
        user_guess = input(" Enter your guess: ").upper()

        if len(user_guess) > pydle.WORD_SIZE:
            print(
                Fore.RED + f"The word '{user_guess}' is greater than "
                f"{pydle.WORD_SIZE} characters... "
                f"You need to guess a {pydle.WORD_SIZE} letter word!"
                + Fore.RESET
                )
            continue

        if len(user_guess) < pydle.WORD_SIZE:
            print(
                Fore.RED + f"The word '{user_guess}' is less than "
                f"{pydle.WORD_SIZE} characters... "
                f"You need to guess a {pydle.WORD_SIZE} letter word!"
                + Fore.RESET
                )
            continue

        pydle.guess(user_guess)
        interface_result(pydle)

        # guess_result = pydle.guess_attempt(user_guess)
        # print(*guess_result, sep="\n")  # Prints each result on new line

    if pydle.correct_guess:
        print(
            Fore.GREEN + f"\nYou guessed correct! "
            f"The hidden word was: {pydle.hidden}" + Fore.RESET
            )
    else:
        print("\nOh no! You've run out of guesses! (5/5)\n")
        print("The word you were trying to solve was: ")
        print(Fore.GREEN + f"{pydle.hidden}\n")
        print(Fore.RED + "GAME OVER")


def interface_result(pydle: Pydle):
    for word in pydle.guesses:
        guess_result = pydle.guess_attempt(word)
        color_string_result = color_interface_result(guess_result)
        print(color_string_result)


def color_interface_result(guess_result: List[CharacterRule]):
    """
    Helper function to store a list of strings and looping through each
    character of the guess_result displaying the result in colour if correct
    and/if correct position.
    """
    color_guess = []
    for letter in color_guess:
        if letter.correct_position:
            letter_color = Fore.CYAN
        elif letter.correct_letter:
            letter_color = Fore.YELLOW
        else:
            letter_color = Fore.WHITE
        character_color = letter_color + letter.word_letter + Fore.RESET
        color_guess.append(character_color)
    return "".join(color_guess)


if __name__ == "__main__":
    main()
