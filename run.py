"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 5 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""

import random
from colorama import Fore  # Library for changing terminal text colour

# Pydle logic functions


class CharacterRule:
    """
    Holds the rules for if the letters are in the hidden word or in the
    correct positon.
    """
    def __init__(self, word_letter: str):  # set 'word_letter' to string
        self.word_letter: str = word_letter
        self.correct_letter: bool = False
        self.correct_position: bool = False

    def __repr__(self):
        """
        function overrides the information displayed in terminal for
        CharacterRule object. Making it easier to read feedback from user
        guess with the correct letter and correct position when debugging.
        """
        return (
            f"[{self.word_letter} correct_letter: {self.correct_letter} "
            f"correct_position: {self.correct_position}]"
        )


class Pydle:
    # Class constants
    WORD_SIZE = 7
    GUESS_MAX = 5

    def __init__(self, hidden: str):  # set argument 'hidden' to string
        self.hidden: str = hidden
        self.guesses = []

    def guess(self, word: str):
        self.guesses.append(word)

    def guess_attempt(self, word: str):
        """
        Compares the user guess against hidden word and gives feedback for the
        letter by looping through the hidden word letter by letter and checking
        if the character is valid.
        """
        guess_result = []  # list of character rules

        for i in range(self.WORD_SIZE):
            character_x = word[i]
            letter = CharacterRule(character_x)
            letter.correct_letter = character_x in self.hidden
            letter.correct_position = character_x == self.hidden[i]
            guess_result.append(letter)

        return guess_result

    @property
    def correct_guess(self):
        """
        True if current guess is equal to the hidden word then win condition
        otherwise False
        """
        return len(self.guesses) > 0 and self.guesses[-1] == self.hidden

    @property
    def guess_remain(self) -> int:  # return as an integer
        return self.GUESS_MAX - len(self.guesses)

    @property
    def guess_still(self):
        """
        When user has used all their guesses or correctly guessed then can no
        longer continue guessing. True when current number of guesses is less
        than the max guess of 5
        """
        return self.guess_remain > 0 and not self.correct_guess

# Pydle interface functions


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
        print("GAME OVER")


def interface_result(pydle: Pydle):
    for word in pydle.guesses:
        guess_result = pydle.guess_attempt(word)


def color_interface_result(guess_result: List[CharacterRule]):
    """
    Helper function to store a list of strings and looping through each
    character of the guess_result displaying the result in colour if correct
    and/if correct position.
    """
    color_guess = []
    for letter in color_guess:
        if letter.correct_position:
            letter_color = Fore.LIGHTBLUE_EX
        elif letter.correct_letter:
            letter_color = Fore.CYAN
        else:
            letter_color = Fore.LIGHTBLACK_EX
        character_color = Fore.RESET + letter.word_letter + letter_color
        color_guess.append(character_color)
    return "".join(color_guess)


def username():
    """
    Function to create the player username for greeting
    """
    # Possibly add a log in prompt here for username and password.
    user = input("To begin playing please enter Your Username: ").capitalize()
    print(f"\nWelcome to Pydle {user}! This is a Python CLI version of the \n"
          "popular game Wordle. In this version you will have 5 attempts \n"
          "at guessing the hidden word. To add an extra challenge, the \n"
          "word you will be guessing is 7 letters long... Good luck!\n")


main()
