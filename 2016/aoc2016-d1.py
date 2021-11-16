di=[]
with open ("/Users/adam/aoc2016-d1.txt") as file:
    for each in file:
        di=each.split(", ")

di[len(di)-1]=di[len(di)-1][:2]  


def part1(inputa):
    xy=[0,0,0]
    for t in inputa:
        if t[:1]=="L":
            if xy[2]==0:
                xy[2]=270
            else:
                xy[2]-=90
        if t[:1]=="R":
            if xy[2]==270:
                xy[2]=0
            else:
                xy[2]+=90
        if xy[2]==90:
            xy[1]+=int(t[1:])
        elif xy[2]==270:
            xy[1]-=int(t[1:])
        elif xy[2]==180:
            xy[0]-=int(t[1:])
        elif xy[2]==0:
            xy[0]+=int(t[1:])
    return xy
        
def part2(inputa):
    xy=[0,0,0]
    li=[0,0]
    for t in inputa:
        if t[:1]=="L":
            if xy[2]==0:
                xy[2]=270
            else:
                xy[2]-=90
        if t[:1]=="R":
            if xy[2]==270:
                xy[2]=0
            else:
                xy[2]+=90
        if xy[2]==90:
            for q in range(int(t[1:])): 
                xy[1]+=1
                if [xy[0],xy[1]] in li:
                    return xy
                li.append([xy[0],xy[1]])
        elif xy[2]==270:
            for q in range(int(t[1:])): 
                xy[1]-=1
                if [xy[0],xy[1]] in li:
                    return xy
                li.append([xy[0],xy[1]])
        elif xy[2]==180:
            for q in range(int(t[1:])): 
                xy[0]-=1
                if [xy[0],xy[1]] in li:
                    return xy
                li.append([xy[0],xy[1]])
        elif xy[2]==0:
            for q in range(int(t[1:])): 
                xy[0]+=1
                if [xy[0],xy[1]] in li:
                    return xy
                li.append([xy[0],xy[1]])
                
    return xy
    
print(part2(di))



