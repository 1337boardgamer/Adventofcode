import csv
with open("/Users/Adam/Desktop/aocd2.csv",newline="") as passwordinput:
    reader=csv.reader(passwordinput)
    password = list(reader)
char = []
lrange = []
for i in range(len(password)):
    password[i]=str(password[i]).replace("[",'').replace("]","")
    password[i]=password[i].replace("'","")
    password[i]=password[i].split(" ")
    char.append(password[i][1])
    lrange.append(password[i][0].split("-"))
    password[i]=password[i][2]
    
correct_count=0

for i in range(len(password)):
    
    pmin=int(lrange[i][0].replace("'",""))
    pmax=int(lrange[i][1].replace("'",""))
    #temp=password[i].count(char[i][0])
    #if temp>=pmin and temp<=pmax:
    #   correct_count=correct_count+1
    if password[i][pmin-1] == char[i][0] and password[i][pmax-1] != char[i][0] or password[i][pmin-1] != char[i][0] and password[i][pmax-1] == char[i][0]:
        correct_count=correct_count+1
    
print(correct_count)






