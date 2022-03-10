"""
pydle_logic.py contains the functions used for the logic of the Pydle game.
Seperate from main run.py for ease of reference within the game code and
to make it easier to read.
"""

from character_rule import CharacterRule


class Pydle:
    # Class constants
    WORD_SIZE = 7
    GUESS_MAX = 5

    def __init__(self, hidden_word: str):  # set argument to string
        self.hidden_word: str = hidden_word
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
            letter.correct_letter = character_x in self.hidden_word
            letter.correct_position = character_x == self.hidden_word[i]
            guess_result.append(letter)

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
        return self.GUESS_MAX - len(self.guesses)

    @property
    def guess_still(self):
        """
        When user has used all their guesses or correctly guessed then can no
        longer continue guessing. True when current number of guesses is less
        than the max guess of 5
        """
        return self.guess_remain > 0 and not self.correct_guess
