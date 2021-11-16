string =[]
with open ("/Users/adam/aoc2016-d2.txt") as file:
    for each in file:
        string.append(str(each).strip())
test=["ULL","RRDDD","LURDL","UUUUD"]
#957DCwrong

def number(c):
    if c[0]==0:
        if c[1]==2:
            return 1
    elif c[0]==1:
        if c[1]==1:
            return 2
        elif c[1]==2:
            return 3
        elif c[1]==3:
            return 4
    if c[0]==2:
        if c[1]==0:
            return 5
        elif c[1]==1:
            return 6
        elif c[1]==2:
            return 7
        elif c[1]==3:
            return 8
        elif c[1]==4:
            return 9
    elif c[0]==3:
        if c[1]==1:
            return "A"
        elif c[1]==2:
            return "B"
        elif c[1]==3:
            return "C"
    if c[0]==4:
        if c[1]==2:
            return "D"
def part1(s):
    x=0
    y=2
    code=""
    for e in s:
        for t in e:
            if t=="L":
                if x==0:
                    pass
                elif y==0 or y==4:
                    pass
                elif (y==1 or y==3) and x==1:
                    pass
                else:
                    x-=1
            elif t=="R":
                if x==4:
                    pass
                elif y==0 or y==4:
                    pass
                elif (y==1 or y==3) and x==3:
                    pass
                else:
                    x+=1
            elif t=="U":
                if y==0:
                    pass
                elif x==0 or x==4:
                    pass
                elif (x==1 or x==3) and y==1:
                    pass
                else:
                    y-=1
            elif t=="D":
                if y==4:
                    pass
                elif x==0 or x==4:
                    pass
                elif (x==1 or x==3) and y==3:
                    pass
                else:
                    y+=1
        code+=str(number([y,x]))
    return code
def part2(s):
    pass
#print(part1(["RU","RRRULU"]))
print(part1(string))
