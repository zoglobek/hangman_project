def chek_if(guess):
    print("ok")

def player_guess():
    guess = str(input("Please input a letter\n"))
    guess = guess.lower()
    if len(guess) == 1:
        if guess.isalpha():
            chek_if(guess)
    else:
        print("Invalid guess")
        print("guess again")
        player_guess()


player_guess()
