#46074 too high
def convert(str1):
    total=0
    for i in range(len(str1)):
        total+=int(str1[i])*pow(2,(len(str1)-1-i))
    return str(total)
def check(strtemp):
    if len(strtemp) <=15 or len(strtemp)>=17:
        return True
    return False
def binary(ints):
    tempw=str(bin(ints))
    tempw=tempw[2:]
    return tempw.zfill(16)   
def AND(str1,str2):
    tempstr=""
    d = str1
    y = str2
    for q in range(len(str2)):
        if d[q] == "1" and y[q]=="1":
            tempstr+="1"
        else:
            tempstr+="0"
    check(tempstr)
    return tempstr
def OR(str1,str2):
    tempstr=""
    d = str1
    y = str2
    for q in range(len(str2)):
        if d[q] == "1" or y[q]=="1":
            tempstr+="1"
        else:
            tempstr+="0"
    return tempstr
def lshift(str1,move):
    tempstr=""
    for b in range(move,len(str1)):
        tempstr+=str1[b]
    for b in range(move):
        tempstr+="0"
    if check(tempstr):
        print(tempstr)
    return tempstr
def rshift(str1,move):
    tempstr=""
    for b in range(move):
        tempstr+="0"
    for b in range(len(str1)-move):
        tempstr+=str1[b]
    if check(tempstr):
        print(tempstr)
    return tempstr
        
def NOT(str1):
    tempstr=""
    for d in str1:
        if d == "1":
            tempstr+="0"
        elif d == "0":
            tempstr+="1"
    check(tempstr)
    return tempstr
def search(valuex,key):
    for p in range(len(valuex)):
        if key == valuex[p][0]:
            return True
    return False
def opvalue(valuex,key):
    for i in range(len(valuex)):
        if key ==valuex[i][0]:
            return valuex[i][1]
    return None

operations = []
values = []

with open ("/Users/Adam/aoc2015-d7.txt") as file:
    for each in file:
        operations.append(each.strip())
values.append(["a",None])
count=0
while count<len(operations):
    
    if operations[count].count(" ")==2:
        temp = operations[count].split(" -> ")
        if temp[0] != 'lx':
            values.append([temp[1],binary(int(temp[0]))])
            operations.pop(count)
        else:
            count+=1
    else:
        count+=1
rounds=0

   
while values[0][1]== None:
    count=0
    rounds+=1
    for each in operations:
        temp = each.split(" -> ")
        operation = temp[0].split(" ")
        store = temp[1]
        op=0
        try:
            operation[0]=int(operation[0])
            operation[0]=str(operation[0])
            op=1
        except:
            pass
        countlower=0
        countvalues=0
        for tempr in operation:
            if tempr.islower():
                countlower+=1
                if search(values,tempr):
                    countvalues+=1
        if countlower==countvalues and operation[0]!="1":
            if countlower + 2==len(operation):
                if operation[1]=="RSHIFT" and countvalues+2==len(operation):
                    values.append([store,rshift(opvalue(values,operation[0]),int(operation[2]))])
                elif operation[1]=="LSHIFT" and countvalues+2==len(operation):
                    values.append([store,lshift(opvalue(values,operation[0]),int(operation[2]))])
            elif operation[0]=="NOT":
                values.append([store,NOT(opvalue(values,operation[1]))])
            elif operation[0] =="lx" and search(values,operation[0]):
                values.append([store,opvalue(values,operation[0])])
            elif operation[1]=="AND":
                values.append([store,AND(opvalue(values,operation[0]),opvalue(values,operation[2]))])
            elif operation[1]=="OR":
                values.append([store,OR(opvalue(values,operation[0]),opvalue(values,operation[2]))])
            elif operation[1]=="XOR":
                pass
            operations.pop(count)
        elif op==1 and (operation[1]=="AND" or operation[1]=="OR") and search(values,operation[2]):
            if operation[1]=="AND":
                values.append([store,AND(binary(int(operation[0])),opvalue(values,operation[2]))])
            #elif operation[1]=="OR":
                #values.append([store,OR(binary(int(operation[0])),opvalue(values,operation[2]))])
            operations.pop(count)
            
        count+=1
    if values[len(values)-1][0]=="a":
        values[0][1]=values[len(values)-1][1]
    #print(values[len(values)-1])        
                
        #print(countvalues, " ", operation, " ",store)
        
        #break



  
values.sort()
for t in values:
    
    print(t[0], " ",convert(t[1]))