import copy
import math


jolts = []
with open ("/Users/Adam/desktop/aocd10.txt", newline="") as jolt:
    for line in jolt:
        jolts.append(int(line))
jolts.sort()
one=0
two=0
three=0
numlist=[]
jolts.insert(0,0)
jolts.append(max(jolts)+3)
for num in range(len(jolts)-1):
    if jolts[num+1] - jolts[num] == 1:
        one = one + 1
    if jolts[num+1] - jolts[num] == 2:
        two = two + 1
    if jolts[num+1] - jolts[num] == 3:
        three = three + 1
        numlist.append(one)
        one=0
com = 1        
for value in numlist:
    if value == 2:
        com = com*2
    if value == 3:
        com = com*4
    if value == 4:
        com = com*7
print(com)
print(numlist)
print(one)
print(three)

    
