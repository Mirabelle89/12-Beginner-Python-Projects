import random
def guess(x,max_guesses):
    random_number=random.randint(1,x)
    num_guesses=0
    while num_guesses <max_guesses:
        num_guesses+=1
        guess_left=max_guesses-num_guesses+1
        print(f"You only have {guess_left} chance.")
        guess=int(input(f"Guess a number betwwen 1 and {x}:  "))
        if guess < random_number:
            print("sorry,guess again,Too low.")
        elif guess > random_number:
            print("sorry,guess again,Too high.")
        else:
            print(f"Yay,congrates.You have guessed the number {random_number}!")
            return
    print(f"Sorry, you ran out of guesses. The number was {random_number}.")
guess(100,5)