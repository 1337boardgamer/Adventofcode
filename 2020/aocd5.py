import csv
import math
with open("/Users/Adam/Desktop/aocd5.csv",newline="") as passwordinput:
    reader=csv.reader(passwordinput)
    password = list(reader)
highid = []
for i in range(len(password)):
    password[i]=str(password[i]).replace("[",'').replace("]","")
    password[i]=password[i].replace("'","")
for i in range(len(password)):
    seatrow = [1,126]
    seatcolumn = [0,7]
    for t in range(len(password[i])):
        if password[i][t] == "F":
            seatrow[1]=seatrow[1]-(math.ceil((seatrow[1]-seatrow[0])/2))
        elif password[i][t] == "B":
            seatrow[0]=seatrow[0]+(math.ceil((seatrow[1]-seatrow[0])/2))
        elif password[i][t] == "L":
            seatcolumn[1]=seatcolumn[1]-(math.ceil((seatcolumn[1]-seatcolumn[0])/2))
        elif password[i][t] == "R":
            seatcolumn[0]=seatcolumn[0]+(math.ceil((seatcolumn[1]-seatcolumn[0])/2))
        else:
            pass
    highid.append(seatrow[0]*8+seatcolumn[0])

print(len(highid))
temp = []
for i in range(1000):
    temp.insert(i,0)
for i in range(len(highid)):
    temp[highid[i]] = 1
for i in range(len(temp)):
    if temp[i] == 0:
        print(i)
    
    
        
        