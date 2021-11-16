import csv
with open('/Users/adam/Desktop/aocd1.csv',newline="") as f:
	reader =csv.reader(f)
	data = list(reader)
for i in range(len(data)):
    data[i]=int(str(data[i]).replace("['",'').replace("']",""))
    temp=data
for i in data:
    for j in temp:
        for k in temp:
            if(i+j+k==2020):
                print(i*j*k)
    temp.pop(0)
                
    