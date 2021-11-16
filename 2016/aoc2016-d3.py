tri=[]
import copy
with open ("/Users/adam/aoc2016-d3.txt") as file:
    for each in file:
        temp=each.strip().split("  ")
        temp2=[]
        for s in temp:
            if s=="":
                pass
            else:
                temp2.append(s)
        tri.append([int(temp2[0]),int(temp2[1]),int(temp2[2])])
            
def part1(t):
    count=0
    for e in t:
        if e[0]+e[1]>e[2] and e[2]+e[1]>e[0] and e[0]+e[2]>e[1]:
            count+=1
            print(count)
    return count
def part2(t):
    count=0
    q=0
    while q<len(t):
        if t[q][0]+t[q+1][0]>t[q+2][0] and t[q][0]+t[q+2][0]>t[q+1][0] and t[q+1][0]+t[q+2][0]>t[q][0]:
            count+=1
        if t[q][1]+t[q+1][1]>t[q+2][1] and t[q][1]+t[q+2][1]>t[q+1][1] and t[q+1][1]+t[q+2][1]>t[q][1]:
            count+=1
        if t[q][2]+t[q+1][2]>t[q+2][2] and t[q][2]+t[q+2][2]>t[q+1][2] and t[q+1][2]+t[q+2][2]>t[q][2]:
            count+=1
        q+=3
    return count

print(part2(tri))