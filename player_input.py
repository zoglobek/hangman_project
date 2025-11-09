def player_guess():
    guess = str(input("Please input a letter"))
    guess = guess.lower()
    if len(guess) == 1:
        check_if()
    else:
        print("Invalid guess")
        print("guess again")
        player_guess()

player_guess()
