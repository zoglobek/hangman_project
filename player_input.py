def check_if(guess):
    print(guess)



def player_guess():
    guess = str(input("Please input a letter\n"))
    guess = guess.lower()
    if len(guess) == 1:
        if guess.isalpha():
            check_if(guess)
    else:
        print("Invalid guess")
        print("guess again")
        player_guess()



if __name__ == '__main__':
    ...