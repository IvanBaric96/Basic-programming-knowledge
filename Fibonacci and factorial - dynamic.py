def FibonacciSequence(n):
    res=[0]*n
    if n==1:
       res[0]=1
       return res
    if n==2:
        res[0]=res[1]=1
        return res
    if n>2:
        res=[0]*n
        res[0]=res[1]=1
        for i in range(2, n):
           res[i]=res[i-1]+res[i-2]
        return res
#print(FibonacciSequence(15))

def Fibonacci(n):
    return FibonacciSequence(n)[n-1]
#print(Fibonacci(15))

def FactorialSequence(n):
    res=[0]*(n+1)
    if n==0:
        res[0]=1
        return res
    else:
        res[0]=1
        for i in range(1,n+1):
            res[i]=i*res[i-1]
        return res
#print(FactorialSequence(10))

def Factorial(n):
    return FactorialSequence(n)[n]
#print(Factorial(10))