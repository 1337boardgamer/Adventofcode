bank=[]
from numpy import base_repr
from copy import deepcopy
#low 727
#too high 2794

with open("/Users/adam/aoc2017-d6.txt") as t:
    for each in t:
        bank=each.strip().split("\t")
def mx(t):
    ma=-1
    l=0
    for s in range(len(t)):
        if int(t[s],36)>ma:
            ma=int(t[s],36)
            l=s
    return l
def distribute(q,w):
    size=int(q[w],36)
    q[w]="0"
    a=w+1
    if a==len(q):
        a=0
    while size>0:

        q[a]=base_repr(int(q[a],36)+1,36)
        size-=1
        a+=1
        if a==len(q):
            a=0
    return q
        
    
def part1(b):
    count=0
    used=[]
    while "".join(b) not in used:
        used.append("".join(b))
        count+=1
        loc=mx(b)
        b=distribute(b,loc)
    print(used, "  ",b)
    return b

for each in range(len(bank)):
    bank[each]=base_repr(int(bank[each]),36)

#print(part1(["B",'B','D',"7",'0','F','5','5','4','4','1','1','7','1','F','G']))   
#print(part1(bank))
def part2(b):
    count=0
    used=[]
    temp="".join(b)
    while count==0 or temp!="".join(b):
        used.append("".join(b))
        count+=1
        loc=mx(b)
        b=distribute(b,loc)
        
        
    print(used, "  ",b)
    return count
print(part2(part1(bank)))
        
        
        
        
    
