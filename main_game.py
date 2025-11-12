from click import clear
import time
from hangman_project.hanged_pics import hangmanpics, hanged_openning
from hangman_project.large_list import guessing_line
from hangman_project.player_input import player_guess
def greet ():
    print(f"{hanged_openning}\nWelcome to the Hangman's game!!!")
    PNAME = input("Please enter your name\n").capitalize()
    print(f"\n\nHi {PNAME} Ready to start?")

if __name__ == '__main__':
    greet()
    time.sleep(2)
    clear()
    print(guessing_line)
    player_guess()

