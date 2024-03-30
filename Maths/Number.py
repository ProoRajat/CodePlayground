# to take a number for user
def user_input():
    return int(input("Enter a number: "))


# return the list which cointain the digits of the number
def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num%10)   # add remender
        num //= 10  # removes the last digit
    return digits


# return the reverse number of the given number
def reverse_number(num):
    reverse = 0
    while num > 0:
        reverse = reverse*10 + num%10   # get last digit(remender) and add it to reverse
        num //= 10  # remove the last digit
    return reverse


# return the sum of all digits
def sum_of_digits(num):
    return sum(get_digits(num)) # get the digits and sum them using sum()

    
def check_armstrong(num):  # number equal to it sum of digits
    if sum_of_digits(num) == num:
        return "Armstrong"
    else:
        return "NOT Armstrong"


def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return "NOT Prime"
    else:
        return "Prime"

'''
First user decide what task he want to perform
We take user responce as number corresponding to the take 
(one or more than one seperated by ',') :- as string
Then convert the string into list cointaining integer corresponding to the task
eg :- 1, 2, 3   to list  (1,2,3)
eg :- 2,    5,7 to list  (2,5,7)
'''
def user_input_to_list(user_input):    
    List = []
    number = '' # tempery variable to store a number
    for x in user_input:
        if x != ',':
            number += x
        else:
            List.append(int(number))
            number=''
    # to add last number to the list since string does not alway contain ',' at the end and the else statement is not able to execute  
    if user_input[-1] != ',':
        List.append(int(number))    # task remaing :- add expetion for non integer

    return List
        
# tofix :- repetation
def what_task(string, num):
    for i in user_input_to_list(string):
        match i:
            case 1:
                print("The reverse of ",num," is ", reverse_number(num))
            case 2:
                print("The sum of digits in the number ", num," is ", sum_of_digits(num))
            case 3:
                print("The number ",num ," is ", check_armstrong(num))
            case 4:
                print("The number ", num, " is ", is_prime(num))

number = user_input()

print("What do you want to do with this number?")
print("1. Calculate reverse\n2. Sum of digits\n3. Check Armstrong\n4. Check prime \n")
taskToDo = input("NOTE: Enter the digit corresponding to the take that you want to perform.\n      To do more than one take seperate the digits with ','.\nYour responce: ")

what_task(taskToDo, number)


