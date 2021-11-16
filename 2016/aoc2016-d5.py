inputa="abbhdwsy"
import hashlib

def part1(q):
    i=0
    t=""
    while 1:
        trying = q + str(i)
        trying = hashlib.md5(trying.encode())
        if str(trying.hexdigest())[:5]=="00000":
            t+=str(trying.hexdigest())[5]
            if len(t)==8:
                return t
        i += 1
def part2(q):
    i=0
    t="--------"
    while 1:
        trying = q + str(i)
        trying = hashlib.md5(trying.encode())
        trying=str(trying.hexdigest())
        if str(trying)[:5]=="00000":
            try:
                temp=int(trying[5])
            except:
                temp=10
            if temp<8 and t[temp]=="-":
                t=t[:temp]+trying[6]+t[temp+1:]
                print(t," ",temp)
            if t.count("-")==0:
                return t
        i += 1
print(part2("abc"))
print(part2(inputa))