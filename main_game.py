import random
import large_list
import player_input
import hangman_ascii
from hangman_project.hangman_ascii import HANGMANPICS
from hangman_project.player_input import player_guess
deadpic = HANGMANPICS[6]
greet = print("Welcome to the Hangman's game!!!\n\n"
              "you have 7 guesses")
print(deadpic)
if __name__ == "__main__":
    greet
    player_guess()



