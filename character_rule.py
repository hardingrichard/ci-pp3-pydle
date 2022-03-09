"""
character_rule.py file holds the class CharacterRule which is imported into
the main run.py file and referred to within functions. CharacterRule was
seperated into its own file to tidy up code and to easily refer to.
"""


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
