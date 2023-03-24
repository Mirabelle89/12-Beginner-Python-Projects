import random

def computer_number(x):
    low=1
    high=x
    shuzi=''
    while shuzi != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        shuzi=input(f"is {guess} too high(h),too low(l),or correct(c)??")
        if shuzi == 'h':
            high = guess - 1
        elif shuzi == 'l':
            low = guess + 1
    print(f"yay,the computer guessed your number,{guess}.correctly!!")

computer_number(100)

