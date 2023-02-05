def ListToNumber(l):
    res=""
    for i in range(0, len(l)):
        res+=str(l[i])
    return res

def NumberToList(n):
    n=str(n)
    res=list()
    for x in n:
        res.append(x)
    return res

def ReverseList(l):
    res=list()
    for i in range(0, len(l)):
        res.append(l[len(l)-i-1])
    return res

def DecimalToBinary(n):
    res=list()
    while n>0:
        res.append(n%2)
        n=n//2
    return int(ListToNumber(ReverseList(res)))
#print(DecimalToBinary(154))

def BinaryToDecimal(number):
    num=ReverseList(NumberToList(number))    
    res=0
    for i in range(0, len(num)):
        res+=(2**i)*int(num[i])
    return res
#print(BinaryToDecimal(100110010))

def DecimalToOctal(n):
    res=list()
    while(n>0):
        res.append(n%8)
        n=n//8
    return(int(ListToNumber(ReverseList(res))))
#print(DecimalToOctal(35631))

def OctalToDecimal(number):
    num=ReverseList(NumberToList(number))
    res=0
    for i in range(0, len(num)):
        res+=(8**i)*int(num[i])
    return res
#print(OctalToDecimal(123456))

rjecnik={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
rjecnik2={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}


def DecimalToHex(n):
    res=list()
    while(n>0):
        res.append(rjecnik[n%16])
        n=n//16
    return(ListToNumber(ReverseList(res)))
#print(DecimalToHex(12345678))

def HexToDecimal(number):
    num=ReverseList(NumberToList(number))
    res=0
    for i in range(0, len(num)):
       res+=(16**i)*int(rjecnik2[num[i]])
    return res
#print(HexToDecimal(DecimalToHex(123456)))

#Substract number in hex and number in dec an write solution in binary
def Task(n1,n2):
    n1=HexToDecimal(n1)
    res=n1-n2
    return DecimalToBinary(res)