# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Description

The aim of this project was to create a Hangman class that could take in a list of words, and optionally number of lives (default = 5), as parameters and run a game of Hangman based on these parameters. I aimed to have each guess produce outcomes based on four scenarios: the user is told the input is invalid (i.e.not a single character or not alphabetical) and would be prompted to try again, the user is told that they've entered an already-guessed character and prompted to try again, the user guesses a character incorrectly and loses a life, or the user guesses correctly and is informed thus.

After each guess, I aimed to display a list of correctly-guessed characters, with underscores indicating the missing letters. This meant that I had to make the number of underscores in the original list equal to the length of the randomly selected word, which was achieved by making a list of a single underscore and multiplying it by the length of the word. More difficult was replacing the underscores with letters in the event of the same letter occuring multiple times in the word, as merely replacing by index number would only account for the first instance. I ultimately overcame this using enumerate to get a list of index numbers at each occurance of a letter in the word, then using iteration to replace underscores in the guessed_word list at the same index values.

I also aimed to have the program stop running upon either success or failure. The former I achieved by writing a congratulations message which print following a check for underscores in the guessed_word list. If there are none, that means they have all been replaced with letters, and thus the word is complete. I exit the loop with break. For failure, the code if checks the player's remaining lives are equal to 0, and if they are then message prints informing the player they have lost, then there is a break. I am considering adding a Try Again? option in case of either victory or defeat, so the player does not need to rerun the code to try again.

## Installation instructions

The file titled 'milestone_5.py' contains the completed code. It is a simple python file, so no installation required, though you'll need the means to run a python file in order to use it.

## Usage instructions

Running the code of milestone_5.py will begin a game of Hangman. The game has 5 lives and a premade 5-item list of fruits. Enter a character when prompted and press the ENTER key to confirm. Winning or losing the game stops the code running, so it must be run again to start a new game. To create your own list or change the number of lives, you need to edit the file.

To edit the word list, go to the second line from the bottom (line 76). You will see "word_list = ["apple", "banana", "orange", "kiwi", "melon"]". Simply edit the words to create your desired list. You may add more words or take them away, just make sure to maintain the formatting. There is no limit to the length of the list nor the number of characters a list element can contain, as this has all been accounted for.

To change the number of lives, go to line 72 and find "num_lives = 5". Change the 5 to your preferred number of lives.

Once the desired changes have been made, save the file and run it again, and it will play a game of hangman with your edits.

## File structure of the project

milestone_5.py: contains the complete code
milestone_4.py: contains an older (functional) version of the code for the creation of the Hangman class
milestone_3.py: contains older code for the check_guess() and ask_for_input() functions, later used in the creation of the Hangman class. It lacks the function whereby it checks for win and lose conditions.
milestone_2.py: establishes some of the basic code to be carried forward, namely importing the random module, creating a word list, picking a random word, and checking for the presence of a character in that word.
README.md: That's the file you're reading right now!

## License information
n/a
