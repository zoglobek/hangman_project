import random
from hangman_project.large_list import dotted_line
from hangman_project.player_input import player_guess
PNAME = input("Please enter your name\n").capitalize()
greet = print(f"Hi {PNAME} Welcome to the Hangman's game!!!")



if __name__ == '__main__':
    greet
    print(dotted_line())
    player_guess()
    print()

