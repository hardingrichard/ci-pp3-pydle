"""
pydle_logic.py contains the functions used for the logic of the Pydle game.
Seperate from main run.py for ease of reference within the game code and
to make it easier to read.
"""
from character_rule import CharacterRule


class Pydle:
    """
    The class Pydle is where the logic to the game is stored with the length
    of the word and the number of guesses the user can make. Loops through
    the range of the length of the word and index of the hidden word.
    """
    # Class constants
    WORD_SIZE = 7
    GUESS_MAX = 7
    VOID_CHARACTER = "*"

    def __init__(self, hidden_word: str):  # set argument to string
        self.hidden_word: str = hidden_word
        self.guesses = []

    def guess(self, word: str):
        """
        Adds user guess attempts to list
        """
        self.guesses.append(word)

    def guess_attempt(self, word: str):
        """
        Compares the user guess against hidden word and gives feedback for the
        letter by looping through the hidden word letter by letter and checking
        if the character is valid.
        """
        # Assigns variable to guess results array with dark letters
        guess_result = [CharacterRule(user_guess) for user_guess in word]

        # Third party code taken and manipulated to fit my requirements
        # Creates a copy of the hidden word
        hidden_remain = list(self.hidden_word)
        for i in range(self.WORD_SIZE):
            letter = guess_result[i]
            if letter.word_letter == hidden_remain[i]:
                letter.correct_position = True
                hidden_remain[i] = self.VOID_CHARACTER

        # Loop to check for letters in white
        for i in range(self.WORD_SIZE):
            letter = guess_result[i]
            # If letter is in correct place then skip
            if letter.correct_position:
                continue

            # If letter is in the word and void index to prevent duplicate
            for dup in range(self.WORD_SIZE):
                if letter.word_letter == hidden_remain[dup]:
                    hidden_remain[dup] = self.VOID_CHARACTER
                    letter.correct_letter = True
                    break

        return guess_result

    @property
    def correct_guess(self):
        """
        True if current guess is equal to the hidden word then win condition
        otherwise False
        """
        return len(self.guesses) > 0 and self.guesses[-1] == self.hidden_word

    @property
    def guess_remain(self) -> int:  # return as an integer
        """
        Function for how many remaining attempts the user has
        """
        return self.GUESS_MAX - len(self.guesses)

    @property
    def guess_still(self):
        """
        When user has used all their guesses or correctly guessed then can no
        longer continue guessing. True when current number of guesses is less
        than the max guess of 5
        """
        return self.guess_remain > 0 and not self.correct_guess
