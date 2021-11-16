#1700863 too high
#1699999 too high
#2034 to low
import math
# def elf(house, elves):
#     if elves==1:
#         return 10
#     else:
#         if house%elves==0:
#             return elf(house,math.floor(elves/2))+elves*10
#         else:
#             return elf(house,math.floor(elves/2))        
inputa=34000000
house = []
house.append([0,0])
house.append([10,1])
house.append([20,1])
temp=1
count=0
presents=0
a=720720
maxi=[0,0]
for i in range(a):
    house.append([i*11,1])
for i in range(1,a):
    if math.floor(a/i)>50:
        house[i][0]=0
        
while presents <inputa:
    presents=a*11
    house.append([a*11,1])
    if a%math.floor(a/2)==0:
        presents+=house[int(a/2)][0]
        house[int(a/2)][1]+=1
    if a%math.floor(a/3)==0:
        presents+=house[int(a/3)][0]
        house[int(a/2)][1]+=1
    if a%2 == 0:
        for t in range(1,int(math.floor(a/4))+1):
            if a%t==0:
                presents+=house[t][0]
                house[t][1] += 1
                if math.floor(a/t)==50:
                    house[t][0]=0
    if presents>=inputa:
        count=a
        a=inputa
        break
    if maxi[0] < presents:
        maxi=[presents,a]
    if a%1000==0:
        print(maxi)
            
    a+=1
            
print(count)        
# while count<100000:
#     presents=i*10
#     temp=0
#     if i%math.floor(i/2)==0:
#         present+=math.floor(i/2)*10
#     t=math.floor(i/3)
#     while t>0:
#         if i%t==0:
#             presents+=t*10
# #    presents=elf(i,i)
#         if t==1:
#             break
#         elif presents>inputa:
#             break
#         else:
#             t-=1
#             
#     if presents>=inputa:
#         lower=i
#         count=0
#         break
#     else:
#         count+=1
#         
#     i+=1
print(count)

