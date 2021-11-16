
def lo(s,p):
    for t in range(len(s)):
        if p==s[t]:
            return t
    return int(p)

def swap(s,p1,p2):
    try:
        p1=int(p1)
        p2=int(p2)
    except:
        p1=lo(s,p1)
        p2=lo(s,p2)
    temp=s[p1]
    s[p1]=s[p2]
    s[p2]=temp
    return s
def rev(s,p1,p2):
    st=""
    try:
        p1=int(p1)
        p2=int(p2)
    except:
        p1=lo(s,p1)
        p2=lo(s,p2)
    if p1>p2:
        temp=p2
        p2=p1
        p1=temp
    for t in reversed(range(p1,p2+1)):
            st+=s[t]
    r=[]
    count=0
    for q in range(len(s)):
        if q<p1 or q>p2:
            r.append(s[q])
        else:
            r.append(st[count])
            count+=1
    return r
def rot(s,d,p1):
    try:
        p1=int(p1)
    except:
        p1=lo(s,p1)
        if p1>3:
            p1+=2
        else:
            p1+=1
    p1 %= len(s)
    for t in range(p1):
        if d=="l":
            s.append(s.pop(0))
        elif d=="r":
            s.insert(0,s.pop(len(s)-1))
    
    return(s)
def move(s,p1,p2):
    try:
        p1=int(p1)
        p2=int(p2)
    except:
        p1=lo(s,p1)
        p2=lo(s,p2)
    s.insert(p2,s.pop(p1))
    return s

def part1(r,instruct):
    for q in instruct:
        temp=q.split(" ")
        if temp[0]=="swap":
            r=swap(r,temp[2],temp[5])
        elif temp[0]=="rotate":
            if temp[1]=="left":
                r=rot(r,"l",temp[2])
            elif temp[1]=="right":
                r=rot(r,"r",temp[2])
            else:
                r=rot(r,"r",temp[len(temp)-1])
        elif temp[0]=="reverse":
            r=rev(r,temp[2],temp[4])
        elif temp[0]=="move":
            r=move(r,temp[2],temp[5])
    return r
instructions = []
with open ("/Users/adam/aoc2016-d22.txt") as file:
    for each in file:
        instructions.append(each.strip())

re=["a","b","c","d","e","f","g","h"]                        

def genlist(p,b,c):
    if(len(c)==0):
        return b
    for i in range(len(c)):
        if i == 0:
            temp = c[i+1:]
        elif i == len(c)-1:
            temp = c[:i]
        else:
            temp = c[:i] + c[i+1:]
        p.append(genlist(p,b+c[i],temp))
    return p

def part2(ins):
    temp=genlist([],"","abcdefgh")
    poss=[]
    for w in temp:
        if len(w)==8:
            poss.append(w)
    answers=[]  
    for t in poss:
        ans = part1(list(t),ins)
        if t == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            print(ans)
        if ans == list("fbgdceah"):   
            answers.append(t)
            print(t)
    return answers
#print(part1(re,instructions))
print(part2(instructions))
#wrong ['c', 'e', 'b', 'd', 'a', 'g', 'h', 'f']
        