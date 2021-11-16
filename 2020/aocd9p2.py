def prev(code,pos):
    for i in range (pos-25,pos):
        for t in range(pos-25,pos):
            if code[i] + code[t] == code[pos]:
                return True
    return False
code = []
position =0;
with open ("/Users/Adam/Desktop/aocd9.txt",newline="") as encode:
    for line in encode:
        code.append(int(line))
num=0
for i in range(25,len(code)):
    if prev(code,i):
        pass
    else:
        position=len(code[:i])
        num = code[i]
        i=len(code)+999
print(num)
print(position)
print(len(code))
numlist = []
for i in range(0,position):
        while sum(numlist)>num:
            numlist.pop(0)
        
        if sum(numlist) < num:
            numlist.append(code[i])
        if sum(numlist)==num:
            i=position+1000
            position=0
    

numlist.sort()
print(sum(numlist)==num)
print(numlist[0]+numlist[len(numlist)-1])

