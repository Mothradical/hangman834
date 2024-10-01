import random

class Hangman:
    '''
    This class is used to create conditions for a game a hangman.
    
    Attributes
        word_list (list): a list of words
        num_lives (int): the number of errors the player can make
        word (str): a word randomly selected from word_list
        word_guessed (list): a list of single-character strings that begins as underscores which are repalced by correctly guessed letters
        num_letters: the number of unique letters remaining
        list_of_guesses: an initially empty list that is appended with guessed letters
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word) # Contents to be replaced with correct guesses

        self.list_of_guesses = [] # New guesses are appended to this list

    def check_guess(self, guess):
        '''
        This function checks a guessed letter against a series of conditions.
        '''
        guess = guess.lower()
        if guess in self.word:
            letter_indices = [index for index, letter in enumerate(self.word) if letter == guess]
            for index in letter_indices:
                self.word_guessed[index] = guess
            print(f"Good guess! {guess} is in the word.")
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)
    
    def ask_for_input(self):
        '''
        This function asks the player for inputs for the game of Hangman.
        The function checks for the validity of the input before running the check_guess() function on the input.
        It runs continuously until either break condition is satisfied, which depends on the outcomes of each instance
        of the check_guess() function.
        This is the function to be accessed by the Hangman class object in order to commence a game of Hangman
        '''
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                self.list_of_guesses.append(guess)
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                if self.num_lives == 0:
                    print("You lost!")
                    break
                elif "_" not in self.word_guessed:
                    print(f"Congratulations. You won the game!\nThe word is '{self.word}'!")
                    break


def play_game(word_list):
    '''
    This function takes in a list of words, creates a hangman object called 'game' using it, and
    begins a game by calling the ask_for_input() function. num_lives is also fed into the
    creation of the object, and can be altered to begin the game with a different number of lives.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.ask_for_input()

word_list = ["apple", "banana", "orange", "kiwi", "melon"]
play_game(word_list)