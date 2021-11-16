#125952 too high
#33814 wrong


temp=""
with open ("/Users/Adam/aoc2015-d12.txt") as file:
    for i in file:
        temp+=str(i)
q=0
curly=0
square=0
delete=0
startpos=0

while q< len(temp):
    if temp[q]=="{" and curly==0:
        curly+=1
        startpos=q
    elif temp[q]=="{" and curly>0:
        curly+=1
    elif temp[q]=="[" and curly==1:
        square+=1
    elif temp[q:q+3]=="red" and curly==1 and square==0:
        delete=1
    elif temp[q]=="}":
        curly-=1
    elif temp[q]=="]"and curly==1:
        square-=1
    if curly==0 and delete==1:
        temp=temp[:startpos]+temp[q+1:]
        q=startpos
        startpos=0
        delete=0
    elif curly==0 and delete==0 and startpos!=0:
        q=startpos
        startpos=0
    if curly<0:
        curly=0
    q+=1
        
q=0
while q < len(temp):
    try:
        int(temp[q])
    except:
        try:
            if temp[q]=="," or temp[q]=="-":
                pass
            else:
                temp=temp[:q]+temp[q+1:]
                q-=1
        except:
            print(len(temp)," ",q)
    q+=1
lists = temp.split(",")
q=0
while q < len(lists):
    if lists[q]=="":
        lists.pop(q)
    else:
        q+=1
count=0
for t in lists:
    count+=int(t)
print(count)