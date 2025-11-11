from click import clear
import time
from hangman_project.hanged_pics import hangmanpics, hanged_openning
from hangman_project.large_list import guessing_line
from hangman_project.player_input import player_guess
def greet ():
    print(hanged_openning)
    PNAME = input("Please enter your name\n").capitalize()
    print(f"\n\nHi {PNAME} \nWelcome to the Hangman's game!!!")

if __name__ == '__main__':
    greet()
    time.sleep(3)
    clear()
    player_guess()
    print(guessing_line)

