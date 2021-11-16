buses = []
with open ("/Users/Adam/Desktop/aocd13.txt") as bus:
    for line in bus:
        buses.append(str(line).strip().split(","))
sch = []
count = 0
for x in range(len(buses[0])):
    if buses[0][x] == "x":
        pass
    else:
       sch.append(str(buses[0][x]) + ","+ str(x))
print(sch)
for each in sch:
    tem=each.split(",")
    print(int(tem[0])-int(tem[1]))
tsch=[]   
for each in sch:
    tsch.append(each.split(","))

notfound = True

#i = 199999547548556
#i =  1204769017

bigm=29*41*37*653*13*17*23*19*823
a = [0,22,14,624,3,12,6,3,763]
n = []
m = [29,41,37,653,13,17,23,19,823]
q=[]
count=0
for each in m:
    n.append((int(bigm/each)) % each)
    q.append((int(bigm/each)))
count = 0
for t in range(len(a)):
    count = count + a[t]*n[t]*q[t]
print(count%bigm)
temp = count%bigm
for each in m:
    print(temp%each)
true=True
find41=True
find37=True
find13=True
find17=True
find23=True
find653=True
find19=True
i=0
tempor=29
while true:
    i = i + tempor
    if find41:
        if (i+19)%41==0:
            tempor= tempor*41
            find41=False
            print("found 41")
    elif find37:
        if (i+23)%37==0:
            tempor=tempor*37
            find37=False
            print("found 37")
    elif find13:
        if (i+42)%13==0:
            tempor=tempor*13
            find13=False
            print("found 13")
    elif find17:
        if (i+46)%17==0:
            tempor=tempor*17
            find17=print("found 17")
    elif find23:
        if (i+52)%23==0:
            tempor=tempor*23
            find23=False
            print("found 23")
    elif find19:
        if (i+79)%19==0:
            tempor=tempor*19
            find19=False
            print("found 19")
    elif find653:
        if (i+29)%653==0:
            tempor=tempor*653
            find653=False
            print("found 653")
    else:
        if (i+60)%823==0:
            true = False
            print("found 823")
            break
    
print(i)
        

    
    