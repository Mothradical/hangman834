# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

Table of Contents (in progress)

The aim of this project was to create a Hangman class that could take in a list of words, and optionally number of lives (dfaults = 5), as parameters
and run a game of Hangman based on these parameters. I aimed to have each guess produce outcomes based on four scenarios: the user is told the input is invalid
(i.e.not a single character or not alphabetical) and would be prompted to try again, the user is told that they've entered an already-guessed character and
prompted to try again, the user guesses a character incorrectly and loses a life, or the user guesses correctly and is informed thus.

After each guess, I aimed to display a list of correctly-guessed characters, with underscores indicating the missing letters. This meant I had to make the number of
underscores in the original list equal to the length of the randomly selected word, which was achieved by making a list of a single underscore and multiplying it
by the length of the word. More difficult was replacing the underscores with letters in the event of the same letter occuring multiple times in the word, as merely
replacing by index number would only account for the first instance. I ultimately overcame this using enumerate to get a list of index numbers at each occurance
of a letter in the word, then using iteration to replace underscores in the guessed_word list at the same index values.

I also aimed to have the program stop running upon either success or failure. The former I achieved by writing a congratulations message which print following
a check for underscores in the guessed_word list. If there are none, that means they have all been replaced with letters, and thus the word is complete. I exit the
loop with break. For failure, the code if checks the player's remaining lives are equal to 0, and if they are a GAME OVER message prints and there is a break.
I am considering adding a  Try Again? option in case of either victory or defeat, so the player does not need to rerun the code to try again.

Installation instructions (in progress)

Usage instructions (in progress)

Run the code of milestone_4.py to create the class! There is a test list at the bottom of the code which creates a 5-item list and gives the player 5 lives,
so just replace the contents of that list with your own and change the desired numbers of lives (it defaults to 5 if you don't set your own) and run the code to
play. There is no limit to the length of the list nor the number of characters a list element can contain, as this has all been accounted for. As of right now, the winning or losing the game ends the code, so it must be run again to start a new game.

File structure of the project (in progress)

License information (in progress)
