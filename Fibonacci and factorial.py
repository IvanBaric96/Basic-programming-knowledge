def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
#print(Fibonacci(23))

def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
#print(Factorial(12))