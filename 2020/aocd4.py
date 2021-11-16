import csv
import math
import re
rehgt= re.compile(r'hgt:\d+(cm|in)')

with open("/Users/Adam/Desktop/aocd4.csv",newline="") as passport:
    for 
    
lastblank=0
increment=0
passport=[]
byr = 0
iyr = 0
eyr = 0
hgt = 0
hcl = 0
ecl = 0
pid = 0
cid = 0

for i in range(len(password)):
    password[i]=str(password[i]).replace("[",'').replace("]","")
    password[i]=password[i].replace("'","")
#for t in range(len(password)):
    #passport[lastblank] = passport[lastblank] + password[t].split(" ")
    #if password[t]=="":
        #lastblank = lastblank + 1
        #passport.append("")
#print(passport[0
##print(re.search('hgt:(\d\d\d|\d\d)(cm|in)',password[6])[0])
#print(password[0][password[0].find("hcl:")+4:password[0].find("hcl:")+7])
for i in range(len(password)):
    temphgt=rehgt.search(password[i])
    if password[i]=="":
        temphgt=rehgt.search(password[i])
        lastblank = lastblank + 1
        if byr != 0 and iyr != 0 and eyr != 0 and hgt != 0 and hcl != 0 and ecl != 0 and pid != 0:
            increment = increment + 1
            
        byr = 0
        iyr = 0
        eyr = 0
        hgt = 0
        hcl = 0
        ecl = 0
        pid = 0
        cid = 0
    else:
        if password[i].find("byr:") == -1:
            pass
        else:
            if int(password[i][password[i].find("byr:")+4:password[i].find("byr:")+8]) >= 1920 and int(password[i][password[i].find("byr:")+4:password[i].find("byr:")+8]) <= 2002:
                byr = 1
        if password[i].find("iyr:") == -1:
            pass
        else:
            if int(password[i][password[i].find("iyr:")+4:password[i].find("iyr:")+8]) >= 2010 and int(password[i][password[i].find("iyr:")+4:password[i].find("iyr:")+8]) <= 2020:
                iyr = 1
        if password[i].find("eyr:") == -1:
            pass
        else:
            if int(password[i][password[i].find("eyr:")+4:password[i].find("eyr:")+8]) >= 2020 and int(password[i][password[i].find("eyr:")+4:password[i].find("eyr:")+8]) <= 2030:
                eyr = 1
        if temphgt:
            temphgt=str(temphgt.group())
            print(temphgt[4:temphgt.find("in")])
            print(temphgt[4:temphgt.find("cm")])
            if temphgt.find("cm")!=-1 and int(temphgt[4:temphgt.find("cm")]) >= 150 and int(temphgt[4:temphgt.find("cm")-1] <= 193):
                hgt = 1
            elif temphgt.find("in")!=-1 and int(temphgt[4:temphgt.find("in")]) >=59 and int(temphgt[4:temphgt.find("in")]-1 <= 76):
                hgt=1
        if password[i].find("hcl:") == -1:
            pass
        else:
            hcl = 1
        if password[i].find("ecl:") == -1:
            pass
        else:
            ecl = 1
        if password[i].find("pid:") == -1:
            pass
        else:
            pid = 1
print(increment)
#print(lastblank)
           
        
        
    