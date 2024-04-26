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
def reverse_of_number(num):
    reverse = 0
    while num > 0:
        reverse = reverse*10 + num%10   # get last digit(remender) and add it to reverse
        num //= 10  # remove the last digit
    return reverse


# return the sum of all digits
def sum_of_digits(num):
    return sum(get_digits(num)) # get the digits and sum them using sum()

    
def check_armstrong(num):  # number equal to it sum of digits
    return True if sum_of_digits(num) == num else False


# check if the number is prime or not
# negative numbers, 0 and 1 are not prime
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                return False
        else:
            return True
    else:
        return False
    

# to check if given number is Palindrome or not
def is_palindrome(num):
    return True if reverse_of_number(num) == num else False


# return divisors in a list
def return_divisors(num):
    divisors = []
    for divisor in range(1,abs(num)+1):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors


# perfect number :- sum of divisors(excuding number) = number
def is_perfect(num):
    if num <= 0:
        return False
    divisors = return_divisors(num)
    divisors.remove(num)
    return True if num == sum(divisors) else False


# returns fibnacci sequence upto n terms as a list
def fibonacci_sequence(num):
    sequence = [0,1]
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    for i in range(0,num-2):
        sequence.append(sequence[i]+sequence[i+1])
    return sequence


# to check if the number is in fibonacci series or not
def is_fibonacci_number(num):
    n = 1
    while fibonacci_sequence(n)[-1] <= num:
        if num == fibonacci_sequence(n)[-1]:
            return True
        n += 1
    else:
        return False

# def is_smith(num):
#     sumOfDigitsOfDivisors = 0
#     for i in return_divisors(num):
#         sumOfDigitsOfDivisors += sum_of_digits(i)
#         print(sumOfDigitsOfDivisors)
#     print(sumOfDigitsOfDivisors - num)
#     return True if sumOfDigitsOfDivisors - num == sum_of_digits(num) else False


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
                print(f"The reverse of {num} is {reverse_of_number(num)}")
            case 2:
                print(f"The sum of digits in the number {num} is {sum_of_digits(num)}")
            case 3:
                if check_armstrong(num):
                    print(f"The number {num} is Armstrong")
                else:
                    print(f"The number {num} is NOT Armstrong")
            case 4:
                if is_prime(num):
                    print(f"The number {num} is Prime")
                else:
                    print(f"The number {num} is NOT Prime")
            case 5:
                if is_palindrome(num):
                    print(f"The number {num} is Palindrome")
                else:
                    print(f"The number {num} is NOT Palindrome")
            case 6:
                print(f"The divisors of {num} are {return_divisors(num)}")
            case 7:
                if is_perfect(num):
                    print(f"The number {num} is Perfect")
                else:
                    print(f"The number {num} is NOT Perfect")
            case 8:
                if fibonacci_sequence(num) == []:
                    print("Please enter a positive number")
                else:
                    print(f"The Fibonacci sequence upto {num} terms is {fibonacci_sequence(num)}")
            case 9:
                if is_fibonacci_number(num):
                    print(f"The number {num} is Fibonacci")
                else:
                    print(f"The number {num} is NOT Fibonacci")
            # case 10:
            #     if is_smith(num):
            #         print(f"The number {num} is Smith")
            #     else:
            #         print(f"The number {num} is NOT Smith")


number = user_input()

print("\nWhat do you want to do with this number?")
print("1. Calculate reverse")
print("2. Sum of digits")
print("3. Check Armstrong")
print("4. Check prime")
print("5. Check Palindrome")
print("6. Print Divisors")
print("7. Check Perfect Number")
print(f"8. Print Fibonacci sequence upto {number} terms")
print("9. Check Fibonacci Number")
# print("10. Check Smith Numbers")

taskToDo = input("NOTE: Enter the digit corresponding to the take that you want to perform.\n      To do more than one take seperate the digits with ','.\nEg :- 1,2,3 or 2 or 5,6\nYour responce: ")
print()

what_task(taskToDo, number)


