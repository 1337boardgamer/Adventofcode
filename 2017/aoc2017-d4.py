count=[]
unique=True
with open("/Users/adam/aoc2017-d4.txt") as file:
    for each in file:
        unique=True
        temp=each.strip().split(" ")   
        for t in temp:
            if temp.count(t)>1:
                unique=False
        if unique:
            w=[]
            for r in temp:
                w.append("".join(sorted(r)))
            count.append(w)
print(len(count))

def part2(s):
    count=0
    for e in s:
        unique=True   
        for t in e:
            if e.count(t)>1:
                unique=False
        if unique:
            count+=1
    return count
print(part2(count))