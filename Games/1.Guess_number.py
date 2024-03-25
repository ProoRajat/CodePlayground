from random import randint
from user_decision import get_user_decision

rand_num = randint(1,10) # Generating a random integer between 1 and 10

while True:
    user_num = int(input("\nGuess a number between 1 and 10: "))
    if rand_num == user_num:
        print("Use Guessed it correct\n")

        # Asking for playing for again or not
        if not get_user_decision("Do you want to play again(y/n): "):
            break

        # x = input("Do you want to play again(y/n): ")
        # if x == 'n':    # Game will only end when x will be n
        #     break
        # else:
        #     rand_num = randint(1,10)
        #     continue
    elif rand_num < user_num:
        print("....Too high....")
    else:
        print("....Too low....")

print("Thanks for Playing")