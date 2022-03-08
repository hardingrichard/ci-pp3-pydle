"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 5 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""

import random


# Pydle interface functions


def main():  # main function placeholder
    username()
    pydle = Pydle("JACUZZI")

    while True:
        # convert user input to uppercase to match against hidden word.
        user_guess = input("\n Enter your guess: ").upper()
        if user_guess == pydle.hidden:
            print(f"You guessed correct! The hidden word was: {pydle.hidden}")
            break
        print("Nope! This wasn't the word.")


def username():
    """
    Function to create the player username for greeting
    """
    # Possibly add a log in prompt here for username and password.
    user = input("To begin playing please enter Your Username: ").capitalize()
    print(f"\nWelcome to Pydle {user}! This is a Python CLI version of the \n"
          "popular game Wordle. In this version you will have 5 attempts \n"
          "at guessing the hidden word. To add an extra challenge, the \n"
          "word you will be guessing is 7 letters long... Good luck!")

# Pydle logic functions


class Pydle:
    # Class constants
    WORD_SIZE = 7
    GUESS_MAX = 5

    def __init__(self, hidden: str):
        self.hidden: str = hidden
        self.guess = []

    def correct_guess(self):
        """
        True if current guess is equal to the hidden word then win condition
        otherwise False
        """
        return self.guess[-1] == self.hidden

    def guess_remain(self):
        """
        When user has used all their guesses or correctly guessed then can no
        longer continue guessing. True when current number of guesses is less
        than the max guess of 5
        """
        return len(self.guess) < self.GUESS_MAX and not self.correct_guess


main()
