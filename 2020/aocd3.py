import csv
with open("/Users/Adam/Desktop/aocd3.csv",newline="") as passwordinput:
    reader=csv.reader(passwordinput)
    password = list(reader)
for i in range(len(password)):
    password[i]=str(password[i]).replace("[",'').replace("]","")
    password[i]=password[i].replace("'","")
width = len(password[0])
slope = [1,1],[3,1],[5,1],[7,1],[1,2]
#slope = [3,1]
trips = 1
for t in range(len(slope)):
    right = 0
    tree = 0
    down=slope[t][1]
    horiz=slope[t][0]
    for i in range(0,len(password),down):
        if password[i][right] == "#":
            tree = tree + 1
        right = right + horiz
        if right>=width:
            temp = right - width
            right=temp
    right=0
    print(tree)
    trips = trips * tree
    tree=0

print(trips)
        
        