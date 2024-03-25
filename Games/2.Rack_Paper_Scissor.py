from random import randint
from user_decision import get_user_decision

def random_output():    # generate 0 = ROCK, 1 = PAPER, 2 = SCISSOR
    x = randint(0,2)
    return 'ROCK' if x == 0 else 'PAPER' if x == 1 else 'SCISSOR'

def message():  # Ask for input
    print("\n....ROCK....")
    print("....PAPER....")
    print("....SCISSOR....")
    return input("Enter your input: \n")

def decision(user, comp):   # calculate who wins
    if user == comp:
        return 'DRAW'
    
    elif user == 'ROCK':
        if comp == 'PAPER':
            return 'COMPUTER WIN'
        elif comp == 'SCISSOR':
            return 'YOU WIN'
        
    elif user == 'PAPER':
        if comp == 'SCISSOR':
            return 'COMPUTER WIN'
        elif comp == 'ROCK':
            return 'YOU WIN'
        
    elif user == 'SCISSOR':
        if comp == 'ROCK':
            return 'COMPUTER WIN'
        elif comp == 'PAPER':
            return 'YOU WIN'
        
    else:   # if user give some other input
        return 'Please Check Your Input'


while True:
    user_input = message().upper()  # take input and convert it to upper case
    comp_input = random_output()    # random computer input

    print("\n------",decision(user_input, comp_input),"------", sep='') # print who win
    print("\nComputer Played '", comp_input,"'", sep='')    # shows the output of comp

    if not get_user_decision("\nDo you want to play again (y/n): "):
        break
    # again = input("\nDo you want to play again (y/n): ")    # ask if want to continue playing
    # if again == 'y' or again == '': # continue even if input is enter key
    #     continue
    # else:
    #     print("##### Thanks for playing #####") # Break in any other case
    #     break

print("##### Thanks for playing #####")