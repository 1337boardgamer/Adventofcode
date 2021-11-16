instructions=[]
with open ("/Users/adam/aoc2016-d22c.txt") as file:
    for each in file:
        temp=[]
        for t in each.split(" "):
            if t !="":
                temp.append(t.strip())
        instructions.append(temp)
        
for r in range(len(instructions)):
    instructions[r][0]=instructions[r][0].split("/")[3]
    instructions[r][0]=[instructions[r][0].split("-")[1][1:],instructions[r][0].split("-")[2][1:]]
    instructions[r][1]=instructions[r][1][:len(instructions[r][1])-1]
    instructions[r][2]=instructions[r][2][:len(instructions[r][2])-1]
    instructions[r][3]=instructions[r][3][:len(instructions[r][3])-1]
def check(s,x,y):
    count=0
    used=s[x][y][1]
    try:
        if used <= s[x-1][y][2]:
           count+=1
    except:
        pass
    try:
        if used <= s[x+1][y][2]:
           count+=1
    except:
        pass
    try:
        if used <= s[x][y-1][2]:
           count+=1
    except:
        pass
    try:
        if used <= s[x][y+1][2]:
           count+=1
    except:
        pass
    return count
        
def part1(ins):
    count=0
    stor=[]
    for i in range(33):
        temp=[]
        for t in range(30):
            temp.append([0,0,0])
        stor.append(temp)
    for t in ins:
        stor[int(t[0][0])][int(t[0][1])][0]=int(t[1])
        stor[int(t[0][0])][int(t[0][1])][1]=int(t[2])
        stor[int(t[0][0])][int(t[0][1])][2]=int(t[3])
    for i in range(33):
        for t in range(30):
            count+=check(stor,i,t)
    print(count)
    count=0
    for i in range(33):
        for t in range(30):
            used=stor[i][t][1]
            for x in range(33):
                for y in range(30):
                    if i==x and y==t:
                        pass
                    elif used==0:
                        pass
                    elif used<stor[x][y][2]:
                        count+=1
    print(count)
part1(instructions)