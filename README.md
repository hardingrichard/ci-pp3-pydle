# Pydle CLI
A Python version of the popular game Wordle played in the command line
interface of the Python terminal. This version consists of a hidden word made
up of 7 characters long where the user will have 7 guesses to find the hidden
word. [Click here to play on the Heroku app](https://pydle-cli.herokuapp.com/)

![Pydle Heroku app terminal](docs/mockup/pydle_terminal.png)

## Table Of Contents

1. [How To Play](#how-to-play)
2. [Key Project Goals](#key-project-goals)
    1. [Site Owner Goals](#site-owner-goals)
    2. [User Goals](#user-goals)
3. [Information Gathering](#information-gathering)
    1. [Target Audience](#target-audience)
    2. [User Requirements](#user-requirements)
    3. [User Stories](#user-stories)
4. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)
    3. [User Interface](#user-interface)
5. [Features](#features)
6. [Technology stack](#technology-stack)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
7. [Testing](#testing)
    1. [Validation](#validation)
    5. [User Story testing](#user-story-testing)
8. [Bugs and Fixes](#bugs-and-fixes)
9. [Deployment and Version Control](#deployment-and-version-control)
10. [Credits and Acknowledgements](#credits-and-acknowledgements)


## How To Play
* To begin, enter the **Username:** *Pydle* **Password:** *password123* exactly
* There is a hidden word that the user must guess which consists of 7
characters in length.
* The user will have 7 attempts to guess the hidden word.
* The user must guess a valid 7 letter word and is unable to submit a random
entry of characters.
* If the guess is not equal to 7 letters then a prompt will display giving
feedback that the incorrect amount of characters was used.
* Begin with the first guess. On submission of first the guess, will display 
the user's entry as well as if the guess has any letters that match the 
hidden word.
* If the letter in the guessed word displays white: The user has guessed the
correct letter but in the wrong position.
* If the letter in the guessed word displays cyan: The user has guessed the
correct letter and is in the correct position.
* If the letter in the guessed word displays grey: The user has guessed an
incorrect letter that is not in the word.
* If all the letters display cyan: User has guessed the correct word and won.
* If the user is unsuccessful then the hidden word will display so that the
user can see what word they were trying to guess. Followed by a Game Over
message.
* To play again click the Run program message at the top of the terminal.

## Key Project Goals

### Site Owner Goals
* To create a simple and engaging game with a replayability factor.
* Users to test their vocabulary and possibly learn new words!
* Have familiarity with the game Wordle so that new users can easily pick up.
and start playing fairly intuitively.
* Provide the user with feedback on their entries and win/loss outcomes.

### User Goals
* Pick up a game that is engaging and challenging to play.
* Simple intuitive design that isn't too confusing and low learning curve.
* Feedback on progress in the game with each guess.
* Want to know what the winning outcome would have been if unsuccessful.
* Replayability factor that can be played multiple times without having the
same word consistently appear.

## Information Gathering

### Target Audience
* The casual gamer who likes to pick up a game to play when bored.
* Education sector as a tool for learning vocabulary and spelling.
* Workers who are looking to play a simple and quick game on their breaks.

### User Requirements
* Have an engaging game to play that is fun and can be replayed.
* Intuitive to play without having a steep learning curve
* Gameplay to work as intended
* Feedback on progress within the game
* If the game was lost, to know what the winning outcome would have been.

### User Stories
No. | As a | I want to | so that
----|------|-----------|--------
1 | user | know how to play the game | I can easily play without confusion.
2 | user | have feedback as I play | I can see what the correct letters are.
3 | user | see the winning outcome | I can see what i was trying to guess if not successful.
4 | user | know that I am guessing valid words | I'm not wasting my guess attempts adding to my user experience.
5 | site owner | provide a description on how to play | users who are not familiar with the game Wordle will know how to play Pydle.
6 | site owner | give feedback of invalid guesses | it will avoid any unnecessary frustrations with users typing invalid words or words not of the correct length without realising.
7 | site owner | display the hidden word on the end of game | users can see what word they were trying to guess if unsuccessful.
8 | site owner | feedback on remaining guesses | to increase the user experience so that they can see how many tries they have left before the game will finish.
9 | site owner | have valid Python code | no errors or bugs are returned to the user.

## Technical Design

### Flowchart
The Pydle flowchart can be seen below. It was created using Lucid Charts.
<details>
<summary>Pydle Flowchart</summary>
<img src="docs/pydle_flowchart.png" alt="Pydle Flowchart image">
</details>

### Data Models
The Pydle application makes use of both functional and object-orientated 
programming in forms of classes, decorators, methods, functions, attributes,
for and while loops as well as lists and dictionaries. 

Two classes were used within the project for the logic of the game, which were
the rules for the letters for the hidden word using booleans and were defined 
as 'Pydle' for the game logic and 'CharacterRule' for the letter rules. 

Lists and dictionaries were used to grab the list of valid words as well as 
a list of words to be used for the hidden words and manipulate them so that
the index of the letters within those words could be iterated.

For and While loops were used to iterate through the list of words 
to be used for the hidden word as well as the letters within the words as an 
index for validation displaying whether a word/letter was correct or not.

The run.py file houses the main function of the game as well as the interface
functions of the game. This was chosen to be the main file from which the game
would be run, importing the logic and rules from the other .py files.

The pydle_logic.py file houses the game logic within the class: Pydle. This
was chosen to be separated from the main run.py file to make it easier to be 
able to read and a less confusing structure. It allowed me to then import this
class into the main file without having to worry about its position within the
structure of the file.

The character_rule.py file is where the class: CharacterRule is held which
defines the rules for if the letters are in the hidden word or the correct
position. It is imported into the main run.py file and referred to within the
functions. It was decided to have its separate file for ease of reference
as well as not having to worry about its position within the structure of the
file.

Two .txt files were used. valid_words.txt holds a list of all the possible 7
letter words that are valid real words. This file was used for validation
purposes so that the user wasn't able to guess words that do not exist or type
random letters to cheat the game. The word_list.txt is a list of 500 of the
most common 7 letter words and is used for choosing a random word from this
list for the hidden word that the user must guess.

### User Interface
The user interface makes use of a simple 'lo fi' aesthetic and limited colours
to be able to provide the user with validation feedback on their inputs, such 
as invalid words or incorrect word lengths typed, resulting in an error message
displayed in red. Positive results such as guessing the correct hidden word 
result in a green message to the user. Colours were also used in order to 
display whether the user has guessed the correct letter within the word or if 
the correctly guessed letter is in the right position. Underscores were used 
to display the length of the characters under the user's guess so that they
could also have visual feedback of remaining guesses as well as having textual 
feedback.

## Features
The Pydle application runs in a terminal and is made up of 7 different features:

### Username Login
<details>
<summary>Username login</summary>
<img src="docs/features/features_username_login.png" alt="login terminal image">
</details>
The username login section requires the user to type in the username and password to gain access to start playing. The username data is sent to and fetched from google sheets via an API.
<details>
<summary>Incorrect login</summary>
<img src="docs/features/features_incorrect_login.png" alt="login terminal image">
</details>
On incorrect login the user is presented feedback notifying of either an incorrect username or password typed and requires the user to re-input the correct login details. <br>
* User stories: 9

### Welcome Message And How To Play
<details>
<summary>Welcome/how to play</summary>
<img src="docs/features/features_welcome_howtoplay.png" alt="How to play terminal image">
</details>
After successfully logging in the user is presented a welcome message and instructions on how to play the game. <br>
* User stories: 1, 5

### User Guess Input And Validation
<details>
<summary>User guess and validation</summary>
<img src="docs/features/features_word_input.png" alt="User guess terminal image">
</details>
The user is required to enter a 7 letter word to try and guess the hidden word. The word must be valid and if not the user will be displayed feedback to let them know if the word is less than 7 characters, more than 7 characters or isn't a valid word. <br>
* User story: 4, 6 

### Tips section
<details>
<summary>User tips</summary>
<img src="docs/features/features_tips.png" alt="User tips section terminal image">
</details>
There is a tips section presented to the user to give them a reminder of what the colour coding for each letter displayed with Blue being correct colour in the correct positon, White being correct letter but in the wrong position and black not being in the word. <br>
* User story: 5

### User interface
<details>
<summary>User interface</summary>
<img src="docs/features/features_interface.png" alt="User interface terminal image">
</details>
The user interface displays the guessed words by the user with each letter colour coded to the tips section. The interface also consists of underscores under the guessed words providing feedback to the user of their progress and an idea of how many attempts remain. There is also a further prompt underneath that gives a clear indication to the use of how many guesses the user has left. <br>
* User story: 2, 4, 8

### End game condition message
<details>
<summary>End game condition</summary>
<img src="docs/features/features_endgame.png" alt="End game terminal image">
</details>
Once the user has guessed the word or has used up all their remaining attempts and end game condition is met and the user is presented with a message letting them know that they were either successful or unsuccessful. It also provides the user with what the hidden word was giving additional user experience. <br>
* User story: 3, 7

## Technology Stack

### Languages
* Python 3

### Frameworks and Tools
* Git
* GitHub
* Gitpod
* Heroku
* Lucidchart
* VS code Pylint
* PEP8online python linter

## Testing

### Validation
The Python code for each .py file was validated using the PEP8 Online
Validation Service. The main run.py file returned with zero errors or
warnings. The pydle_logic.py file and the character_rule.py file both
returned with the E701 - multiple statements on one line (colon) weak 
warning code. When googling this warning code it appears that it could 
be a bug and has been reported by multiple users.
<details>
<summary>run.py</summary>
<img src="docs/validation/runpy_pep8_validation.png" alt="run.py pep8 validation image">
</details>

<details>
<summary>pydle_logic.py</summary>
<img src="docs/validation/pydle_logic_pep8_validation.png" alt="pydle_logic.py pep8 validation image">
</details>

<details>
<summary>character_rule.py</summary>
<img src="docs/validation/character_rule_pep8_validation.png" alt="character_rule.py pep8 validation image">
</details>

<details>
<summary>VS code Pylint</summary>
<img src="docs/validation/vscode_pylint_terminal.png" alt="VS code Pylint validation image">
</details>

### User Story Testing
Testing of the User Stories which had been identified towards the top of the README are as follows:
>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  1 | user | know how to play the game | I can easily play without confusion.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
How to play | Successfully log in | On successful log in a how to play message is displayed | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  2 | user | have feedback as I play | I can see what the correct letters are.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
User interface | Successfully log in and make a guess entry and hit enter | On making a guess a dispaly is shown with the word guessed with each letter colour coded to whether the letter is correct, in the right position or not in the word | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  3 | user | see the winning outcome | I can see what i was trying to guess if not successful.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
End game condition message | Successfully log in, made 7 word guesses as unable to find the hidden word | A message was displayed notifying "Oh no! You've run out of guesses! (7/7) The word you were tyring to solve was: FEELING" | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  4 | user | know that I am guessing valid words | I'm not wasting my guess attempts adding to my user experience.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
User guess input and validation | Successfully log in then make an attempt at guessing the word. | If a word was input which is less  than 7 characters or greater than 7 characters in length an error message is displayed giving feedback notifying this. If a nonsense word is typed that doesn't exist an error message is displayed with feedback notifying that the word is invalid and no guess attempts were used for these. | Worked as intended.
User interface | Successfully log in and make attempts at guessing. | On valid word entries i can see the word is logged and is valid and that the guesses remaining prompt corresponds | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  5 | site owner | provide a description on how to play | users who are not familiar with the game Wordle will know how to play Pydle.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
How to play | Successfully log in | a welcome message and paragraph is displayed describing how to play the game | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  6 | site owner | give feedback of invalid guesses | it will avoid any unnecessary frustrations with users typing invalid words or words not of the correct length without realising.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
User guess input and validation | Successfully log in then make an attempt at guessing the word. | If a word was input which is less  than 7 characters or greater than 7 characters in length an error message is displayed giving feedback notifying this. If a nonsense word is typed that doesn't exist an error message is displayed with feedback notifying that the word is invalid and no guess attempts were used for these. | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  7 | site owner | display the hidden word on the end of game | users can see what word they were trying to guess if unsuccessful.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
End game condition message | Successfully log in, made 7 word guesses as unable to find the hidden word | A message was displayed notifying "Oh no! You've run out of guesses! (7/7) The word you were tyring to solve was: FEELING" | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  8 | site owner | feedback on remaining guesses | to increase the user experience so that they can see how many tries they have left before the game will finish.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
User interface | Successfully log in and make attempts at guessing. | On valid word entries i can see the word is logged and under are lines of underscores giving an indication of how many guess attempts remain. There is also a prompt at the bottom detailing how many guesses remain | Worked as intended.

>  No. | As a | I want to | so that
>  ----|------|-----------|--------
>  9 | site owner | have valid Python code | no errors or bugs are returned to the user.

Site Feature | Path of Action | Outcome | Testing Result
-------------|----------------|---------|----------------
User log in | Attempt to log in | On unsuccessful log in the code validation kicks in notifying the user that the incorrect username and/or password was typed and restarts the login process. On successful log in the application displays a successfully logged in message and advances to the instructions on how to play | Worked as intended.


## Bugs and Fixes
I had an issue spanning a couple of days trying to get the pygame module to work. Receiving a pygame.error: no available video device. After reaching out and logging a tutor support ticket, realised that this module wouldn't work with the terminal and ended up scrapping the repository and starting fresh with a CLI version instead of a GUI application. The project was met with multiple bugs during the process and some of which were documented and shown below.

BUG | FIX
----|----
Class object was being printed in the terminal as an object instead of the constructor instance name. | Changed the f-string from '{pydle}' to {pydle.hidden_word}. This then printed the word letters rather than an object name.
Index out of range - tried to access an index of guessed word but no element. | Check if length > 0 and last guess == hidden_word.
Type error '>' not supported between instances of 'method' and 'int'. | Add decorators to the method then used an int return annotation.
Syntax error closing parenthesis ']' does not match opening parenthesis '('. | Deleted the type in error of ']' that was stopping code from running.
Index error: string index out of range. | In the for loop for 'guess_attempt' function, 'word[i]' wasn't put into an argument of the CharacterRule class.
On trying to colour the result of the user guess. Colour isn't working and instead was producing blank lines. | I had referred to the wrong parameter of 'color_guess' instead of 'guess_result' on changing this fixed the terminal output.
unboundLocalError: local variable 'correct_user_details' referenced before assignment. | This was a scope issue and fixed by nesting the if/else statement containing this variable within the prior if/else statement.
W1514 - Using open without explicitly specifying an encoding. | Added 'encoding=utf8' to the file handler due to local encoding and not using utf8 by default.

## Deployment and Version Control

### Deployment
The Pydle application was deployed from Github using Heroku app. To deploy your application please complete the following:

1. Create an account at heroku.com
2. Create a new app 
3. Add the app name and your region
4. Click on create App
5. Go to "Settings"
6. Under Config Vars, add the key: PORT and the value: 8000.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to build your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Cloning
If you wish to clone the repository you can do so by [clicking here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or completing the following:
1. Locate and click on the Code button at the top of the directory within the GitHub repository
2. This will drop down the option of HTTPS, SSH, and GitHub CLI and the option to open with GitHub Desktop or Download ZIP. Choose the option you prefer and click the copy to clipboard button
3. Open the Git bash terminal
4. Choose the working directory location to where you wish to have the cloned directory.
5. Type "git clone" followed by pasting the URL you copied in step 2.
6. Press Enter to complete and create your local clone.

### Version Control
[Click here](https://github.com/hardingrichard/ci-pp3-pydle/commits/main) to explore the history of the creation process and see what the code looked like at different points in time and what changes were made. Regular commits were made to make it easier to view the thought process during the creation of the application and readme and also have saved backup points to avoid loss of work in case of any serious malfunctions.

## Credits and Acknowledgements

### Credits
I made use of multiple sources of information, guides and tutorials during the course of the project in order to gain understanding and solve issues that I had. These can be seen listed below:
* Various Stack Overflow topics
* Use of map() - (https://www.realpython.com/python-map-function/)
* Classes and objects - (https://www.w3schools.com/python/python_classes.asp)
* Constructors - (https://pythonbasics.org/constructor/)
* Youtube Pixegami tutorial - (https://youtu.be/SyWeex-S6d0)
* Youtube 3Blue1Brown tutorial - (https://www.youtube.com/watch?v=fRed0Xmc2Wg)
* Decorators - (https://realpython.com/primer-on-python-decorators/)
* Colorama and printing coloured text - (https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python)
* Int: return annotations - (https://docs.python.org/3/library/typing.html)
* Python type hints - (https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* Python type hints 2 - (https://docs.python.org/3/library/typing.html)
* Python tutorial - (https://docs.python.org/3/tutorial/)
* Password masking with pwinput - (https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered)

### Acknowledgements
I would like to give a moment to thank:
* My parents for testing the application as first-time users to see if they found the game intuitive.
* My mentor Mo Shami for his time, guidance, and feedback during our meetings.
* Tutor support for answering a query that had me stuck for a couple of days.
* My cohort on slack for responding to questions.