import random

word_list = ["Apple", "Banana", "Orange", "Kiwi", "Melon"]

print(word_list)

word = random.choice(word_list)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")