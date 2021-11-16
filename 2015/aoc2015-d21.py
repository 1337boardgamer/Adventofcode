def check(m,b):
    temp1=b[0]
    temp2=m[0]
    while temp2>0 and temp1>0:
        if m[1]<=b[2]:
            temp1-=1
        else:
            temp1=temp1-(m[1]-b[2])
        
        if temp1<=0:
            return False
        else:
            if m[2]>=b[1]:
                temp2-=1
            else:
                temp2-=(b[1]-m[2])    
    return True
import copy

weapons=[[8,4],[10,5],[25,6],[40,7],[74,8]]
armor=[[0,0],[13,1],[31,2],[53,3],[75,4],[102,5]]
wrings=[[0,0],[25,1],[50,2],[100,3]]
arings=[[0,0],[80,3],[20,1],[40,2]]
boss=[103,9,2]
me=[100,0,0]
mini=0
com=[]
print(check([100,7,4],boss))
# for each in weapons:
#     
#     for eachs in armor:
#         tempring = copy.deepcopy(wrings)
#         for t in tempring:
#             for x in arings:
#                 if check([me[0],each[1]+t[1],eachs[1]+x[1]],boss):
#                     if each[0]+eachs[0]+x[0]+t[0]>=mini:
#                         mini=each[0]+eachs[0]+x[0]+t[0]
#                         com=[each,eachs,x,t]
#             tempring.pop(0)
#             for u in tempring:
#                 if check([me[0],each[1]+t[1]+u[1],eachs[1]],boss):
#                     if each[0]+eachs[0]+t[0]+u[0]>=mini:
#                         mini=each[0]+eachs[0]+t[0]+u[0]
#                         com=[each,eachs,t,u]
#         tempring = copy.deepcopy(arings)
#         for w in tempring:
#             tempring.pop(0)
#             for q in tempring:
#                 if check([me[0],each[1],eachs[1]+w[1]+q[1]],boss):
#                     if each[0]+eachs[0]+w[0]+q[0]>=mini:
#                         mini=each[0]+eachs[0]+w[0]+q[0]
#                         com=[each,eachs,w,q]
#             
#             
# print(mini)
# print(com)
#                 
    
