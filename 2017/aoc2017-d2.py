num=[]
with open("/Users/adam/aoc2017-d2.txt") as file:
    for each in file:
        num.append(each.strip().split("\t"))
num1 =[]
for q in num:
    temp=[]
    for p in q:
        temp.append(int(p))
    num1.append(temp)
print(num1)
def part1(n):
    total=0
    for t in n:
        total+=(max(t)-min(t))
    return total

print(part1(num1))

def part2(n):
    total=0
    for each in n:
        for p in range(len(each)):
            temp=each[p]
            for r in range(len(each)):
                if each[r]%temp==0 and r!=p:
                    total+=each[r]/temp
                    
                
    return total
print(part2(num1))
print(part2([[5,9,2,8],
[9,4,7,3],
[3,8,6,5]]))
            