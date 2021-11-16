jump=[]
with open("/Users/adam/aoc2017-d5.txt") as f:
    for each in f:
        jump.append(int(each.strip()))
i=0
count=0
while i < len(jump):
    t=jump[i]
    if t>2:
        jump[i]-=1
        i+=jump[i]+1
    else:
        jump[i]+=1
        i+=jump[i]-1
    count+=1
print(count)