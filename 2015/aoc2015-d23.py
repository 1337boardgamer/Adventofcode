instruction = [
"jio a, 18",
"inc a",
"tpl a",
"inc a",
"tpl a",
"tpl a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"tpl a",
"tpl a",
"inc a",
"jmp 22",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"jio a, 8",
"inc b",
"jie a",
"tpl a",
"inc a",
"jmp 2",
"hlf a",
"jmp -7"]
a,b=1,0
i=0
print(instruction[i])
while (i<len(instruction)):
    if instruction[i][:3]=="jie":
        if a%2==0:
            i+=4
            a /=2
        i+=1
    elif instruction[i][:3]=="jio":   
        if a == 1 and instruction[i]=="jio a, 8":
            i+=8
        elif a == 1 and instruction[i]=="jio a, 18":
            i+=18
        else:
            i+=1
    elif instruction[i]=="jmp 22":
        i+=22
    elif instruction[i]=="jmp 2":
        i+=2
    elif instruction[i]=="jmp -7":
        i-=7
    elif instruction[i]=="inc a":
        a+=1
        i+=1
    elif instruction[i]=="inc b":
        b+=1
        i+=1
    elif instruction[i]=="tpl a":
        a*=3
        i+=1
    elif instruction[i]=="tpl b":
        b*=3
        i+=1
    else:
        i+=1
print (b)
        
        