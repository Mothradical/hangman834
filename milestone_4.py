import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_', '_', '_', '_', '_'] # Contents to be replaced with correct guesses
        self.num_letters = len(set(word_list))
        self.list_of_guesses = [] # New guesses are appended to this list

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            letter_indices = [index for index, letter in enumerate(self.word) if letter == guess]
            for index in letter_indices:
                self.word_guessed[index] = guess
            print(f"Good guess! {guess} is in the word.")
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
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

hangman_test = Hangman(["apple", "banana"], 5)

hangman_test.ask_for_input()

