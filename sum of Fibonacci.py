def FibonacciSequence(n):
    res=[0]*n
    if n==1:
       res[0]=1
       return res
    if n==2:
        res[0]=res[1]=1
        return res
    if n>2:
        res[0]=res[1]=1
        for i in range(2, n):
           res[i]=res[i-1]+res[i-2]
        return res
#print(FibonacciSequence(10))

def SumOfArray(arr):
    s=0
    for i in range(len(arr)):
        s+=arr[i]
    return s

def SumOfFibonacciSequence(n):
    return SumOfArray(FibonacciSequence(n))
#print(SumOfFibonacciSequence(10))