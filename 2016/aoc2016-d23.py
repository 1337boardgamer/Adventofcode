code=[]
with open ("/Users/adam/aoc2016-d23.txt") as file:
    for each in file:
        code.append(each.strip())
def part1(co):
    a=12
    b=0
    c=0
    d=0
    step=0
    while step<len(co):
        temp=co[step].split(" ")
        if temp[0]=="cpy":
            if temp[1]=="a":
                if temp[2]=="b":
                    b=a
                elif temp[2]=="c":
                    c=a
                elif temp[2]=="d":
                    d=a
            elif temp[1]=="b":
                if temp[2]=="a":
                    a=b
                elif temp[2]=="c":
                    c=b
                elif temp[2]=="d":
                    d=b
            elif temp[1]=="c":
                if temp[2]=="b":
                    b=c
                elif temp[2]=="a":
                    a=c
                elif temp[2]=="d":
                    d=c
            elif temp[1]=="d":
                if temp[2]=="b":
                    b=d
                elif temp[2]=="c":
                    c=d
                elif temp[2]=="a":
                    a=d
            else:
                if temp[2]=="b":
                    b=int(temp[1])
                elif temp[2]=="c":
                    c=int(temp[1])
                elif temp[2]=="a":
                    a=int(temp[1])
                elif temp[2]=="d":
                    d=int(temp[1])
        elif temp[0]=="dec":
            if temp[1]=="b":
                b-=1
            elif temp[1]=="c":
                c-=1
            elif temp[1]=="a":
                a-=1
            elif temp[1]=="d":
                d-=1
        elif temp[0]=="inc":
            if temp[1]=="b":
                b+=1
            elif temp[1]=="c":
                c+=1
            elif temp[1]=="a":
                a+=1
            elif temp[1]=="d":
                d+=1
        elif temp[0]=="jnz":
            if temp[1]=="b":
                if b!=0:
                    try:
                        step+=int(temp[2])
                    except:
                        if temp[2]=="b":
                            if b==0:
                                step+=1
                            step+=b
                        elif temp[2]=="c":
                            if c==0:
                                step+=1
                            step+=c
                        elif temp[2]=="a":
                            if a==0:
                                step+=1
                            step+=a
                        elif temp[2]=="d":
                            if d==0:
                                step+=1
                            step+=d
                else:
                    step+=1
            
            elif temp[1]=="c":
                if c!=0:
                    try:
                        step+=int(temp[2])
                    except:
                        if temp[2]=="b":
                            if b==0:
                                step+=1
                            step+=b
                        elif temp[2]=="c":
                            if c==0:
                                step+=1
                            step+=c
                        elif temp[2]=="a":
                            if a==0:
                                step+=1
                            step+=a
                        elif temp[2]=="d":
                            if d==0:
                                step+=1
                            step+=d
                else:
                    step+=1
            elif temp[1]=="a":
                if a!=0:
                    try:
                        step+=int(temp[2])
                    except:
                        if temp[2]=="b":
                            if b==0:
                                step+=1
                            step+=b
                        elif temp[2]=="c":
                            if c==0:
                                step+=1
                            step+=c
                        elif temp[2]=="a":
                            if a==0:
                                step+=1
                            step+=a
                        elif temp[2]=="d":
                            if d==0:
                                step+=1
                            step+=d
                else:
                    step+=1
            elif temp[1]=="d":
                if d!=0:
                    try:
                        step+=int(temp[2])
                    except:
                        if temp[2]=="b":
                            if b==0:
                                step+=1
                            step+=b
                        elif temp[2]=="c":
                            if c==0:
                                step+=1
                            step+=c
                        elif temp[2]=="a":
                            if a==0:
                                step+=1
                            step+=a
                        elif temp[2]=="d":
                            if d==0:
                                step+=1
                            step+=d
                else:
                    step+=1
            elif temp[1]!="0":
                try:
                    step+=int(temp[2])
                except:
                    if temp[2]=="b":
                        if b==0:
                            step+=1
                        step+=b
                    elif temp[2]=="c":
                        if c==0:
                            step+=1
                        step+=c
                    elif temp[2]=="a":
                        if a==0:
                            step+=1
                        step+=a
                    elif temp[2]=="d":
                        if d==0:
                            step+=1
                        step+=d
                    
            else:
                step+=1
        elif temp[0]=="tgl":
            num=0
            if temp[1]=="b":
                num=b
            elif temp[1]=="c":
                num=c
            elif temp[1]=="a":
                num=a
            elif temp[1]=="d":
                num=d
            try:
                if co[step+num].count(" ")==1:
                    if co[step+num][:3]=="inc":
                        co[step+num]="dec"+co[step+num][3:]
                    else:
                        co[step+num]="inc"+co[step+num][3:]
                elif co[step+num].count(" ")==2:
                    if co[step+num][:3]=="jnz":
                        co[step+num]="cpy"+co[step+num][3:]
                    else:
                        co[step+num]="jnz"+co[step+num][3:]
            except:
                pass
        if temp[0]=="jnz":
            pass
        else:
            step+=1
    return a


print(part1(code))
                
        
        