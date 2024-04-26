from random import randint
import time

def table():
    num = int(input("\nEnter a number: "))
    n = 1
    while n <= 10:
        print(num, ' x ', n, ' = ', num * n)
        n += 1


def practice():
    difficulty = input("\nSelect Difficulty\nEasy\nMedium\nHard\nExtreme\n-->").upper()
    print("Answer the following: ")
    x = 0
    correct = 0

    if difficulty == 'EASY':
        lowerlimit1, upperlimit1, lowerlimit2, upperlimit2 = 2, 10, 2, 10
    elif difficulty == 'MEDIUM':
        lowerlimit1, upperlimit1, lowerlimit2, upperlimit2 = 2, 99, 11, 99
    elif difficulty == 'HARD':
        lowerlimit1, upperlimit1, lowerlimit2, upperlimit2 = 100, 999, 101, 999
    elif difficulty == 'EXTREME':
        lowerlimit1, upperlimit1, lowerlimit2, upperlimit2 = 1001, 9999, 1001, 9999
    else:
        print("Something went wrong with your input. Please try again!!!")
        practice()
    init = time.time()
    while x < 10:
        a = randint(lowerlimit1, upperlimit1)
        b = randint(lowerlimit2, upperlimit2)
        ab = int(input(f"{a} x {b} = "))
        if ab == a*b:
            correct += 1
            print("--correct--")
        else:
            print("--incorrect!!!--")
        x += 1

    T = time.time() - init
    print(f"You got {correct} correct and {x - correct} wrong")
    print("Time taken: ", int(T),"sec")


def whatTODO():
    n = input("Do you want to print the table of a number (y/n):  ")
    if n in ('Y', 'y', '', 1):
        table()
    n = input("Do you want to practice tables (y/n): ")
    if n in ('Y', 'y', '', 1):
        practice()


whatTODO()