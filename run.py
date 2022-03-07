"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 5 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""

import random


def username():
    """
    Function to create the player username for greeting
    """
    user = input("Please Enter Your Username: ").capitalize()
    print(f"\nWelcome to Pydle {user}! This is a Python CLI version of the \n"
          "popular game Wordle. In this version you will have 5 attempts \n"
          "at guessing the hidden word. To add an extra challenge, the \n"
          "word you will be guessing is 7 letters long... Good luck!")


def main():  # main function placeholder
    username()


main()
