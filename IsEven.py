def IsEven(n):
    if n==2 or n==0:
        print("Number is even!")
    elif n==1:
        print("Number is odd!")
    else:
        if n<0:
            return IsEven(n+2)
        else:
            return IsEven(n-2)
#IsEven(-152)