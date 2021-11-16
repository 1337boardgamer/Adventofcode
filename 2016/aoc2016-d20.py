import copy
ip=[]
with open ("/Users/adam/aoc2016-d20.txt") as file:
    for each in file:
        a=each.strip().split("-")
        ip.append([int(a[0]),int(a[1])])
        
ip.sort()
def part1(ip):
    hi=0
    lo=0
    cip=[]
    t=0
    for t in range(len(ip)-1):
        if hi==0 and lo==0:
            hi=ip[t][1]
            lo=ip[t][0]
        if hi>ip[t+1][0]:
            if hi<ip[t+1][1]:
                hi=ip[t+1][1]
        else:
            cip.append([lo,hi])
            lo=0
            hi=0
    if hi!=0:
        cip.append([lo,hi])
    count=0
    i=0
    true=True
    while i<4294967295:
        
        if true and cip!=[]:
            low,hi=cip.pop(0)
        if i==low:
            i=hi
            true=True
        else:
            count+=1
            true=False
        i+=1      
    return count
print(part1(ip))
print(part2(hi))
#too high 1023924764 881604484
#to low 1888889