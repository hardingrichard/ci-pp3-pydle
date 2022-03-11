"""
Pydle - A python CLI version of the popular Wordle game

The game is a simple word game where the user must find the hidden word by
making guesses at what is thought the hidden word could be. This version Pydle
consists of words made up of 7 letters and the user will have 7 attempts
instead of 6 at guessing the correct word or the game will result in a loss.
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
import random
# 3rd party:
from typing import List
from colorama import Fore  # Library for changing terminal text colour
import pwinput
import gspread
from google.oauth2.service_account import Credentials
# Internal:
from character_rule import CharacterRule
from pydle_logic import Pydle
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google API constants
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("users_logins")
DATA_OF_LOGINS = SHEET.worksheet('login_data')


def user_login():
    """
    Function where the user inputs a username and password which is
    referenced against google sheets for login data.
    """
    print(Fore.MAGENTA + "\n**** PYDLE USER LOG IN TERMINAL **** \n")
    print(
          Fore.RESET + "Before you can start playing. Please log in below"
          " using your username and password details.\n" + Fore.YELLOW +
          "Please Note: username and password details are case sensitive.\n"
          + Fore.RESET
          )

    username = input("Please enter username: \n" + Fore.MAGENTA)
    # pwinput masks the password when typing and changes to '*'
    password = pwinput.pwinput(Fore.RESET + "\nPlease enter Password: \n" +
                               Fore.MAGENTA
                               )
    login = retrieve_user_login()

    # Check username and if it does not match userid then restart loop
    if [value for value in login if value["userid"] != username]:
        print(Fore.RED + "\nIncorrect Username. Login was unsuccessful.")
        print("Please re-enter your details and try again" + Fore.RESET)
        user_login()
    else:
        correct_userdetails = [
            value for value in login if value["userid"] == username
            ][0]

    # Check for password match then log user in and proceed to welcome message
    # If password doesn't match print incorrect feedback to user and restart
        if password == correct_userdetails["passwordid"]:
            print(Fore.GREEN + "\nYou have successfully logged in." +
                  Fore.RESET
                  )
            welcome()
        else:
            print(Fore.RED + "\nIncorrect password. Login was unsuccessful.")
            print("Please re-enter your details and try again" + Fore.RESET)
            user_login()


def retrieve_user_login() -> list:
    """
    Function which takes the user login details from the google sheets
    returning as a list of lists.
    """
    login_info = DATA_OF_LOGINS.get_all_records()
    return login_info


def welcome():
    """
    Function to print a welcome message to the user with information on how
    to play Pydle
    """
    print("\n--------------------------------")
    print(Fore.MAGENTA + "\nWELCOME TO PYDLE \n" + Fore.RESET)
    print("--------------------------------\n")
    print(Fore.WHITE + "This is a Python CLI version of the popular game\n"
          "Wordle. In this version you will have 7 attempts at guessing the\n"
          "hidden word. If you guess the correct letter but in the wrong\n"
          "space then the letter will turn white. If you guess the correct\n"
          "letter and it is in the right position then the letter will turn\n"
          "blue. To add an extra challenge, the word you will be guessing\n"
          "is also 7 letters long..." + Fore.GREEN +
          " GOOD LUCK!\n" + Fore.RESET
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
                f"You need to guess a {pydle.WORD_SIZE} letter word!" +
                Fore.RESET
                )
            continue

        if len(user_guess) < pydle.WORD_SIZE:  # Character length validation
            print(
                Fore.RED + f"The word '{user_guess}' is less than "
                f"{pydle.WORD_SIZE} characters... "
                f"You need to guess a {pydle.WORD_SIZE} letter word!" +
                Fore.RESET
                )
            continue

        if user_guess not in valid_words:  # validation for real 7 letter word
            print(
                Fore.RED + f"{user_guess} doesn't exist or isn't a valid" +
                "word" + Fore.RESET
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
        print("\n Oh no! You've run out of guesses!" + Fore.RED + " (7/7)\n" +
              Fore.RESET
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
    with open(path, "r", encoding="utf8") as file:
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
    with open(path, "r", encoding="utf8") as file:
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


user_login()
main()
