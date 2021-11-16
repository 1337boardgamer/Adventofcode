
rain=[[8,8,53],[13,4,49],[20,7,132],[12,4,43],[9,5,38],[10,4,37],[3,37,76],[9,12,97],[37,1,36]]
#rain=[[14,10,127],[16,11,162]]
maxi = 0
distance=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for i in range(0,2503):
    for t in range(len(rain)):
        if i%(rain[t][1]+rain[t][2])<rain[t][1]:
            distance[t][0]+=rain[t][0]
    for each in distance:
        if maxi<each[0]:
            maxi=each[0]
    for e in range(len(distance)):
        if distance[e][0]==maxi:
            distance[e][1]+=1
maxi=0
for each in distance:
    if each[1]>maxi:
        maxi=each[1]
print(maxi)