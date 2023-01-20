def IsPrime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
#print(IsPrime(53))


def PrimesUnderN(n):
    res=list()
    for i in range(2, n+1):
        if IsPrime(i):
            res.append(i)
    return res
#print(PrimesUnderN(31))

def ReduceFraction(num,den):
    if den==0:
        return "Error!"
    if num==0:
        return 0
    if num==den:
        return 1
    primes=PrimesUnderN(abs(num))
    for p in primes:
        while num%p==0 and den%p==0:
            num=num//p
            den=den//p
    if num<0 and den<0:
        return (-num, -den)
    else:
        return (num, den)
#print(ReduceFraction(21,-1))

def SubstractAndReduce(n_1, d_1, n_2, d_2):
    den=d_1*d_2
    num=d_2*n_1-d_1*n_2
    return(ReduceFraction(num, den))
#print(SubstractAndReduce(-4,-7,3,-8))

def AddAndReduce(n_1, d_1, n_2, d_2):
    den=d_1*d_2
    num=d_2*n_1+d_1*n_2
    return(ReduceFraction(num, den))
#print(AddAndReduce(-4,-7,3,-8))