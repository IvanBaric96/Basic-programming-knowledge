import random
def CreateArray(leng, min=0, max=10):
    arr=[0]*leng
    for i in range(0,leng):
        arr[i]=random.randint(min, max)
    return arr
#print(CreateArray(5))


def SumOfArray(arr):
    s=0
    for x in arr:
        s=s+x
    return s
# a=CreateArray(6)
# print(a)
# print(SumOfArray(a))

def AverageOfArray(arr):
    if len(arr)==0:
      return 0
    else:
        return SumOfArray(arr)/len(arr)
# a=CreateArray(6)
# print(a)
# print(AverageOfArray(a))

import itertools
def SubarraysOfArray(arr):
    res=list()
    for i in range(0, len(arr)+1):
        for combination in itertools.combinations(arr, i):
            res.append(combination)
    return res
# a=CreateArray(4)
# print(a)
# print(SubarraysOfArray(a))

avg=int(input("Unesite vrijednost: "))
def LongestArrayAvg(average,l):
    max_arr=[0]
    a=CreateArray(l)
    print(a)
    print(SubarraysOfArray(a))
    for arr in SubarraysOfArray(a):
        if AverageOfArray(arr)< avg:
            max_arr=arr
    return max_arr

print(LongestArrayAvg(avg,5))
            


