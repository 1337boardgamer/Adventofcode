check=[]
from operator import itemgetter
with open ("/Users/adam/aoc2016-d4.txt") as file:
    for each in file:
        temp=each.split("[")
        check.append([temp[0],temp[1][:5]])
def sort(m):
    for r in range(len(m)):
        for i in range(len(m)):
            if r==i:
                pass
            elif m[r][1]<m[i][1] and r<i:
                swap=m[r]
                m[r]=m[i]
                m[i]=swap
            elif m[r][1]==m[i][1]:
                if m[r][0]>m[i][0] and r<i:
                    swap=m[r]
                    m[r]=m[i]
                    m[i]=swap
    return m
                         
def part1(c):
    total=0
    for t in c:
        temp=''.join(set(t[0]))
        most=[]
        for e in temp:
            try:
                if e == "-":
                    pass
                elif int(e):
                    pass
            except:
                most.append([e,t[0].count(e)])
        most=sort(most)

        if most[0][0]==t[1][0] and most[1][0]==t[1][1] and most[2][0]==t[1][2] and most[3][0]==t[1][3] and most[4][0]==t[1][4]:
            b=t[0].rsplit("-")
            total+=int(b[len(b)-1])
    return total
test=[["aaaaa-bbb-z-y-x-123","abxyz"],["a-b-c-d-e-f-g-h-987","abcde"],["not-a-real-room-404","oarel"],["totally-real-room-200","decoy"]]
#print(part1(check))
#print(part1(test))
def part2(c):
    total=[]
    letters="abcdefghijklmnopqrstuvwxyz"
    for t in c:
        temp=''.join(set(t[0]))
        most=[]
        for e in temp:
            try:
                if e == "-":
                    pass
                elif int(e):
                    pass
            except:
                most.append([e,t[0].count(e)])
        most=sort(most)

        if most[0][0]==t[1][0] and most[1][0]==t[1][1] and most[2][0]==t[1][2] and most[3][0]==t[1][3] and most[4][0]==t[1][4]:
            b=t[0].rsplit("-")
            tr=t[0]
            u=int(b[len(b)-1])%26
            bs=""
            for f in tr:
                try:
                    bs+=letters[(letters.index(f)+u)%26]
                except:
                    bs+=f
            total.append(bs)
    return total
print(part2(check))