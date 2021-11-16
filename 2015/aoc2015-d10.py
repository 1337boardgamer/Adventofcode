a = "3113322113"
#a = "11"
for i in range(50):
    tempstr=""
    count=1
    tempnum=a[0]
    for b in range(1,len(a)):
        if tempnum==a[b]:
            count+=1
            if(b+1==len(a)):
                tempstr+=str(count)
                tempstr+=tempnum    
        else:
            tempstr+=str(count)
            tempstr+=tempnum
            count=1
            tempnum=a[b]
            if(b+1==len(a)):
                tempstr+=str(count)
                tempstr+=tempnum
    a=tempstr
print(len(a))