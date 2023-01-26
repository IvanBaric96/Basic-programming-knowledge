import random
def Common(arr1,arr2):
    s=0
    for i in range(0,len(arr1)):
        if arr1[i] in arr2:
            s+=1
    return s

def ChoiceOfPlayer(n):
    choice=[-1000]*n
    for i in range(n):
        n=int(input("Your number: "))
        while n<1 or n>39:
            print("Your number must be between 1 and 39!")
            n=int(input("Your number: "))
        while n in choice:
            print("You have already chosen this number!")
            n=int(input("Your number: "))
        choice[i]=n
    return choice

def ChoiceOfComputer(n, nums):
    random_numbers=[0]*n
    for i in range(7):
        index=random.randint(0,len(nums))
        random_numbers[i]=nums[index]
        nums.remove(nums[index])
    return random_numbers
    
def ConcatenareArrays(arr1,arr2):
    l=len(arr1)+len(arr2)
    res=[0]*l
    for i in range(0,l):
        if i<len(arr1):
            res[i]=arr1[i]
        else:
            i=i-len(arr1)
            res[i+len(arr1)]=arr2[i]
    return res
# a=[0,1,2,3]
# b=[4,5,6]
# print(ConcatenareArrays(a,b))

def Lottery():   
    numbers=[i for i in range(1,40)]
    ch=ChoiceOfPlayer(7)
    rn=ChoiceOfComputer(7, numbers)  
    print(rn)  
    c=Common(ch, rn)
    if c<=4 or c==7:
        print("Imali ste "+str(c)+" pogodaka! Kraj!")
    elif c==5 or c==6:
        ch_2=ChoiceOfPlayer(3)
        rn_2=ChoiceOfComputer(3,numbers)
        ch_total=ConcatenareArrays(ch,ch_2)
        rn_total=ConcatenareArrays(rn, rn_2)
        if c<=4 or c==7:
           print("Imali ste "+str(c)+" pogodaka! Kraj!")
        
Lottery()

    