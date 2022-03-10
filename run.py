"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 5 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""
import random
from typing import List
from colorama import Fore  # Library for changing terminal text colour
from character_rule import CharacterRule
from pydle_logic import Pydle


def username():
    """
    Function to create the player username for greeting
    """
    # Possibly add a log in prompt here for username and password.
    print(" ")
    user = input("To begin playing please enter Your Username: ").capitalize()
    print("\n--------------------------------")
    print(Fore.WHITE + "\nWelcome to Pydle " + Fore.BLUE + f"{user}! "
          + Fore.WHITE + "This is a Python CLI version of the \n"
          "popular game Wordle. In this version you will have 7 attempts \n"
          "at guessing the hidden word. If you guess the correct letter but\n"
          "in the wrong space then the letter will turn white. If you guess\n"
          "the correct letter and it is in the right position then the\n"
          "letter will turn blue. To add an extra challenge, the \n"
          "word you will be guessing is 7 letters long..." + Fore.GREEN +
          " Good luck!\n" + Fore.RESET
          )
    print("--------------------------------\n")


def main():
    """
    Main function of the file houses user prompts for the interface
    as well as looping through validation checks for user guesses with word
    length and checks for if word is a valid 7 letter word, with the results
    of the user guesses and game outcome printed if correct or unsuccessful.
    """
    pydle_set = load_pydle_list("data/word_list.txt")
    valid_words = load_valid_list("data/valid_words.txt")
    hidden_word = random.choice(list(pydle_set))
    pydle = Pydle(hidden_word)

    while pydle.guess_still:
        # convert user input to uppercase to match against hidden word.
        user_guess = input(
            Fore.YELLOW + "\nEnter your guess: " + Fore.RESET
            ).upper()

        if len(user_guess) > pydle.WORD_SIZE:  # Character length validation
            print(
                Fore.RED + f"The word '{user_guess}' is greater than "
                f"{pydle.WORD_SIZE} characters... "
                f"You need to guess a {pydle.WORD_SIZE} letter word!"
                + Fore.RESET
                )
            continue

        if len(user_guess) < pydle.WORD_SIZE:  # Character length validation
            print(
                Fore.RED + f"The word '{user_guess}' is less than "
                f"{pydle.WORD_SIZE} characters... "
                f"You need to guess a {pydle.WORD_SIZE} letter word!"
                + Fore.RESET
                )
            continue

        if user_guess not in valid_words:  # validation for real 7 letter word
            print(
                Fore.RED + f"{user_guess} doesn't exist or isn't a valid word"
                + Fore.RESET
            )
            continue

        pydle.guess(user_guess)
        interface_result(pydle)

    if pydle.correct_guess:
        print("--------------------------------")
        print(
            "\n You guessed correctly! \n" + Fore.RESET +
            " The hidden word was: " + Fore.GREEN + f"{pydle.hidden_word}\n" +
            Fore.RESET
            )
        print("--------------------------------")
    else:
        print("\n--------------------------------")
        print("\n Oh no! You've run out of guesses!" + Fore.RED + " (5/5)\n"
              + Fore.RESET
              )
        print(" The word you were trying to solve was: " + Fore.GREEN +
              f"{pydle.hidden_word}\n" + Fore.RESET
              )
        print("--------------------------------")
        print(Fore.RED + "\n GAME OVER\n" + Fore.RESET)
        print("--------------------------------\n")


def load_pydle_list(path: str):
    """
    Function reads the word_list.txt file and adds to the list of words to be
    guessed by the user. It will take this list and make them uppercase for
    validation.
    """
    pydle_set = set()
    with open(path, "r") as file:
        for line in file.readlines():
            pydle_words = line.strip().upper()
            pydle_set.add(pydle_words)
    return pydle_set


def load_valid_list(path: str):
    """
    Function reads the valid_words.txt file for a list of all possible valid
    words that are of 7 characters in length and is checked for validation
    against the users guessses in the main function.
    """
    valid_set = set()
    with open(path, "r") as file:
        for line in file.readlines():
            valid_words = line.strip().upper()
            valid_set.add(valid_words)
    return valid_set


def interface_result(pydle: Pydle):
    """
    Prints the interface presented to the player with a player hint and
    colours the user guess and remaining guesses shown as underscores.
    """
    print("\nTip:")
    print("--------------------------------")
    print(Fore.CYAN + " Correct letter in position")
    print(Fore.WHITE + " Correct letter not in position")
    print(Fore.LIGHTBLACK_EX + " Incorrect letter not in word" + Fore.RESET)
    print("--------------------------------\n")

    for word in pydle.guesses:
        guess_result = pydle.guess_attempt(word)
        color_string_result = color_interface_result(guess_result)
        print(" " * 8 + color_string_result + "\n")

    for _ in range(pydle.guess_remain):
        print(" " * 8 + "_ " * pydle.WORD_SIZE + "\n")

    print(f"\nRemaining guesses... {pydle.guess_remain}\n")


def color_interface_result(guess_result: List[CharacterRule]):
    """
    Helper function to store a list of strings and looping through each
    character of the guess_result displaying the result in colour if correct
    and/if correct position.
    """
    color_guess = []
    for letter in guess_result:
        if letter.correct_position:
            letter_color = Fore.CYAN
        elif letter.correct_letter:
            letter_color = Fore.WHITE
        else:
            letter_color = Fore.LIGHTBLACK_EX
        character_color = letter_color + letter.word_letter + Fore.RESET
        color_guess.append(character_color)
    return " ".join(color_guess)


username()
main()
