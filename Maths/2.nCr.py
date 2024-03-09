# nCr = number of ways of selecting r objects from n objects
# nCr = n!/(n-r)!(r)!

# from 1.Factorial
def factorial(n):
    return n*factorial(n-1) if n != 0 else 1

def nCr(n, r):
    return int( factorial(n) / (factorial(n-r)*factorial(r)) )

total = int(input("Total objects: "))
select = int(input("Objects to be selected: "))

print(nCr(total, select))