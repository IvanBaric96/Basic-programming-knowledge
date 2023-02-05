months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def How_Many_Days(d1,m1,y1, d2,m2,y2):
    prvi=False
    total=0
    if y1 < y2:
        return How_Many_Days(d2,m2,y2,d1,m1,y1)
        prvi=True
    elif y1==y2:
        if m1<m2:
            return How_Many_Days(d2,m2,y2,d1,m1,y1)
            prvi=True
        elif m1==m2:
            if d1<d2:
                return How_Many_Days(d2,m2,y2,d1,m1,y1)
                prvi=True
            else:
                return d1-d2
        else:
            for i in range(m2+1, m1):
                total+=months[i]
            total+=months[m2]-d2+d1
            return total
    else: #y1>y2
        total=0
        for i in range(y2+1,y1):
            total+=365
        total+=months[m2]-d2
        for i in range(m2+1,13):
            total+=months[i]
        for i in range(1,m1):
            total+=months[i]
        total+=d1
        return total,prvi

days, flag=How_Many_Days(15,3,1998,18,4,1999)
print("Difference in days is: "+str(days))
if flag==True:
    print("Second person is older!")
else: 
    print("First person is older!")