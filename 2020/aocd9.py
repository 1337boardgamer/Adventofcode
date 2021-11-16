def prev(code,pos):
    for i in range (pos-5,pos):
        for t in range(pos-5,pos):
            if code[i] + code[t] == code[pos]:
                return True
    return False
code = []
position =0;
with open ("/Users/Adam/Desktop/aocd9tmp.txt",newline="") as encode:
    for line in encode:
        code.append(int(line.strip()))
num=0
for i in range(5,len(code)):
    if prev(code,i):
        pass
    else:
        position=len(code[:i])
        num = code[i]
        i=len(code)+999
print(num)
numlist = []
for i in range(0,position):
        if sum(numlist)>127:
            code.pop(0)
            i=0
            numlist.clear()
        if sum(numlist) < 127:
            numlist.append(code[i])
        if sum(numlist)==127:
            i=647

numlist.sort()
print(sum(numlist))
print(numlist[0]+numlist[len(numlist)-1])

