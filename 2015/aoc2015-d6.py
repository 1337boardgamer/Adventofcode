
ops = []
with open ("/Users/Adam/aoc2015-d6.txt") as file:
    for each in file:
        temp=each.split(" ")
        if each.count(" ") == 4:
            ops.append([temp[0]+" "+temp[1],temp[2],temp[4].strip()])
        else:
            ops.append([temp[0],temp[1],temp[3].strip()])
lights = []
for sizey in range(1000):
    temp=[]
    for sizex in range(1000):
        temp.append(0)
    lights.append(temp)
   
for temp in ops:
    startpos=temp[1].split(",")
    finishpos=temp[2].split(",")
    i=int(startpos[0])
    
    if temp[0]=="turn on":
        while i<=int(finishpos[0]):
            t=int(startpos[1])
            while t<=int(finishpos[1]):
                lights[i][t]+=1
                t+=1
            i+=1
    elif temp[0]=="turn off":
        while i<=int(finishpos[0]):
            t=int(startpos[1])
            while t<=int(finishpos[1]):
                if lights[i][t]<=0:
                    lights[i][t]=0
                else:
                    lights[i][t]-=1
                t+=1
            i+=1
    elif temp[0]=="toggle":
        while i<=int(finishpos[0]):
            t=int(startpos[1])
            while t<=int(finishpos[1]):
                lights[i][t]+=2
                t+=1
            i+=1
count=0
for i in range(1000):
    for t in range(1000):
        count+=lights[i][t]
    
print(count)