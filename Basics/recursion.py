def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(5))

def fib(n):
    if(n == 2):
        return 1
    elif(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))