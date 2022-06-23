# step 1

word_list=["ardvark", "baboon", "camel"]

#TODO - 1 - randomaly choose a word from the word_list and assign it to a variable called choosen word
import random

chosen_word=random.choice(word_list)

#TODO -2 - ask the user to guess  a letter and assign their answer to a variables called guess . make guess lowercase.
guess = input("guess a letter : ").lower()

# TODO - 3 - check if the letter the user  guessed (guess) is one of the letters in the chosen word .

for letter in chosen_word:
    if letter==guess:
        print("right")
    else:
        print("wrong")