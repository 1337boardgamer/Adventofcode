#1602 low
#11520 high
#2499 wrong
#1747 wrong
#4299 wrong
# def total(con):
#     tot=0
#     for i in con:
#         tot+=i
#     return tot
#        
# 
# 
containers=[47, 46, 36, 36, 32, 32, 31, 30, 28, 26, 19, 15, 11, 11, 5, 3, 3, 3, 1, 1]
#containers=[20,15,10,5,5,3,1]
size = 150

count = 0
coun=0
small = 0
steps=0
used=[]
mini=99
for i in range(1048575):
    test=str(bin(i))[2:].zfill(20)
    total=0
    for t in range(len(containers)):
        if test[t]=="1":
            total+=containers[t]
    if total==size:
        count+=1
        if test.count("1")<mini:
            mini=test.count("1")
        if test.count("1")==4:
            coun+=1
        
print(coun, " ", mini)
# values=[]
# for i in containers:
#     total = i
#     containers.pop(0)
#     startpos=0
#     t=0
#     steps=0
#     temp=str(i)
#     for t in range(len(containers)-):
#         total=i
#         if containers[t]+total>size:
#             pass
#         elif containers[t]+total==size:
#             count+=1
#         elif containers[t]+total<size:
#             total+=containers[t]
#             for q in range(t+1,len(containers)):
#                 total=i+containers[t]
#                 if containers[q]+total>size:
#                     pass
#                 elif containers[q]+total==size:
#                     count+=1
#                 elif containers[q]+total<size:
#                     total+=containers[q]
#                     for a in range(q+1,len(containers)):
#                         total=i+containers[t]+containers[q]
#                         if containers[a]+total>size:
#                             pass
#                         elif containers[a]+total==size:
#                             count+=1
#                         elif containers[a]+total<size:
#                             total+=containers[a]
#                             w=a+1
#                             startpos=w
#                             while w < len(containers):
#                                 
#                                 if containers[w]+total>size:
#                                     pass
#                                 elif containers[w]+total==size:
#                                     count+=1
#                                 elif containers[w]+total<size:
#                                     total+=containers[w]
#                                     steps+=1
#                                 if w+1==len(containers) and steps!=0:
#                                     startpos+=1
#                                     w=startpos
#                                     total=i+containers[t]+containers[q]+containers[a]
#                                     print(count)
#                                     steps=0
#                                 else:
#                                     w+=1
# for t in range(len(containers)):
#     used=[containers[t]]
#     steps=t+1
#     start=steps
#     startmax=[]
#     maxmax=1
#     maxstep=len(used)
#     maxsteps=False
#     while steps<len(containers):
#         if containers[steps]+total(used)<=size:
#             used.append(containers[steps])
#             if total(used)==size:
#                 count+=1
#                 used.pop(len(used)-1)
#             maxstep=len(used)
#             if maxstep>maxmax:
#                 maxmax=maxstep
#                 if maxstep>2:
#                     startmax.append(steps)
#                     maxsteps=True
#             
#     
#         elif containers[steps]+total(used)>size:
#             pass
#         if steps +1==len(containers):
#             if startmax==[]:
#                 startmax.append(start)
#             if used[len(used)-2]==containers[len(containers)-2] and used[len(used)-1]==container[len(container)-1] and maxsteps:
#                     startmax.pop(len(startmax)-1)
#                     startmax.pop(len(startmax)-1)
#             for i in reversed(range(startmax[len(startmax)-1]-1,len(used))):
#                 used.pop(i)
#             if maxsteps:
#                 if startmax[len(startmax)-2]==containers[len(containers)-2] and startmax[len(startmax)-1]==container[len(container)-1]:
#                     startmax.pop(len(startmax)-1)
#                     startmax.pop(len(startmax)-1)
#                 maxmax=len(used)
#                 steps=startmax.pop()
#                 if len(used)<3:
#                     maxsteps=False
#             else:
#                 steps=start+1
#                 start+=1
#         else:
#             steps+=1
#     print(count)
#         
#         
#             
#         
#                         
# print(count)
#     