# factorial = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    return n*factorial(n-1) if n != 0 else 1

    '''Alternative
    if n != 0:
        return n*factorial(n-1)
    else 1:
    '''

num = int(input("Enter a number: "))

print("The factorial of ", num, "is: ", factorial(num))