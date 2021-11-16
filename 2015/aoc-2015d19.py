#from collections import Counter
def add2string(string,inserts,location,size):
    listss = []
    for teach in inserts:
        #try:
        listss.append(string[:location] + teach + string[location+size:])
        #except:
            #lists.append(string[:location] + each)
    return listss
    # 257 to low
    # 635 to high
    

al = ["ThF","ThRnFar"]
b = ["BCa","TiB","TiRnFAr"]
ca = ["CaCa","PB","PRnFAr","SiRnFYFAr","SiRnMgAr","SiTh"]
f = ["CaF","PMg","SiAl"]
h = ["CRnAlAr","CRnFYFYFAr","CRnFYMgAr","CRnMgYFAr","HCa","NRnFYFAr","NRnMgAr","NTh","OB","ORnFAr"]
mg = ["BF","TiMg"]
n = ["CRnFAR","HSi"]
o = ["CRnFAr","CRnMgAr","HP","NRnFAr","OTi"]
p = ["CaP","PTi","SiRnFAr"]
si = ["CaSi"]
th = ["ThCa"]
ti = ["BP","TiTi"]
e = ["HF","NAl","OMg"]

inputa = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
#inputa = "AlThSiRnTi"
lists = []
count=0
count+=inputa.count("")
for i in range(len(inputa)):
    temp=""
    if inputa[i].isupper():
        if inputa[i+1].islower():
            temp = inputa[i:i+2]
        else:
            temp = inputa[i]
        if temp == "Al":
            for temps in add2string(inputa,al,i,2):
                lists.append(temps)
        elif temp == "B":
            for temps in add2string(inputa,b,i,1):
                lists.append(temps)
        elif temp == "Ca":
            for temps in add2string(inputa,ca,i,2):
                lists.append(temps)
        elif temp == "F":
            for temps in add2string(inputa,f,i,1):
                lists.append(temps)
        elif temp == "H":
            for temps in add2string(inputa,h,i,1):
                lists.append(temps)
                
        elif temp == "Mg":
            for temps in add2string(inputa,mg,i,2):
                lists.append(temps)
        elif temp == "N":
            for temps in add2string(inputa,n,i,1):
                lists.append(temps)
        elif temp == "O":
            for temps in add2string(inputa,o,i,1):
                lists.append(temps)
        elif temp == "P":
            for temps in add2string(inputa,p,i,1):
                lists.append(temps)
        elif temp == "Si":
            for temps in add2string(inputa,si,i,2):
                lists.append(temps)
        elif temp == "Th":
            for temps in add2string(inputa,th,i,2):
                lists.append(temps)
        elif temp == "Ti":
            for temps in add2string(inputa,ti,i,2):
                lists.append(temps)
    
    
lst1=[]
t=len(lists)
for each in lists:
    if each not in lst1:
        lst1.append(each)
def searchstring(string,sub):
    c=[]
    for t in sub:
        c.append(string.count(t))
    return c
def replace(string,occur,sub,value):
    find=string.find(sub)
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != occur:
        # find + 1 means we start searching from after the last match
        find = string.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == occur:
        return string[:find] + value + string[find+len(sub):]
    return string       
                     
                     
                
    
    

print(len(lst1))
lis=[]
lis.append(inputa)
count=1
true=True
while true:
    templis=[]
    for temp in lis:
        r=searchstring(temp,al)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,al[q],"Al"))
        r=searchstring(temp,b)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,b[q],"B"))
        r=searchstring(temp,ca)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,ca[q],"Ca"))
        r=searchstring(temp,f)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,f[q],"F"))
        r=searchstring(temp,h)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,h[q],"H"))
        r=searchstring(temp,n)
        for q in range(len(r)):
            if r[q]>0:
                for t in range(q):
                    templis.append(replace(temp,y+1,n[q],"N"))
        r=searchstring(temp,o)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,o[q],"O"))
        r=searchstring(temp,p)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,p[q],"P"))
        r=searchstring(temp,si)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,si[q],"Si"))
        r=searchstring(temp,th)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,th[q],"Th"))
        r=searchstring(temp,ti)
        for q in range(len(r)):
            if r[q]>0:
                for y in range(q):
                    templis.append(replace(temp,y+1,ti[q],"Ti"))
        
    lis=[]
    count+=1
    mini=1000
    for each in templis:
        if each not in lis:
            if each=="HF" or each == "OMg" or each=="NAl" :
                print(count)
                true=False
            elif len(each):
                lis.append(each)
                if len(each)<mini:
                    mini=len(each)
                    
                        
            
        
  
    print(count, "   ", mini)
    
    
