tree=[]
with open ("/Users/adam/aoc2017-d7.txt") as t:
    for each in t:
        temp=each.strip().split(" ")
        if len(temp)<3:
            tree.append([temp[0],str(temp[1])[1:len(str(temp[1]))-1]])
        else:
            test=[temp[0],str(temp[1])[1:len(str(temp[1]))-1]]
            for r in range(3,len(temp)):
                if "," in temp[r]:
                    test.append(temp[r][:len(temp[r])-1])
                else:
                    test.append(temp[r][:len(temp[r])])
            tree.append(test)
print(len(tree))
def part1(tr):
    temp=[]
    for w in tr:
        if len(w)>2:
            temp.append(w)
    for i in range(len(temp)):
        te=temp[i][0]
        count=0
        
        for e in range(len(tr)):
            if te in tr[e]:
                count+=1
        if count==1:
            return te
        
    return None
start="vmpywg"#part1(tree)
def part2(tr,s="vmpywg"):
    temp=[]
    leaves=[]
    answer=[]
    answer=['vmpywg', ['ykkcei', 'azyzcr', 'ywmuda', 'ndjsvna'], [['espnx', 'wqcsem', 'sgknjo', 'sczhwf', 'dbkkk', 'obxht', 'etyuvh'], ['hciyw', 'pihmrxm', 'ywgvt', 'dcdqv', 'dieqdax', 'fszzls'], ['sswubza', 'jjsvzup', 'hriuldj', 'nddyl', 'rhlbu', 'ruukc'], ['orflty', 'upcttms', 'cdllr']]]
    count=2
#     for w in tr:
#         if len(w)>2:
#             temp.append(w)
#         else:
#             leaves.append(w)
    while count<7:
        ttr=[]
        t = count
        if len(answer)==1:
            trew=answer[0]
            for e in range(1148,len(tr)):
                if tr[e][0]==trew:
                    for r in range(2,len(tr[e])):
                        ttr.append(tr[e][r])
            
        else:
            for r2 in answer[t]:
                tt=[]
                if isinstance(r2,str):
               
                    for e in range(len(tr)):
                        if tr[e][0]==r2:
                            if len(tr[e])>2:
                                for r in range(2,len(tr[e])):
                                    tt.append(tr[e][r])
                            else:
                                tt.append(tr[e][0])
                else:
                    for q in r2:
                        for e in range(len(tr)):
                            if tr[e][0]==q:
                                if len(tr[e])>2:
                                    for r in range(2,len(tr[e])):
                                        tt.append(tr[e][r])
                                else:
                                    tt.append(tr[e][0])
                ttr.append(tt)
                                        
                        
                   
                
        answer.append(ttr)
        count+=1
    count-=2
    total=[]
    print(answer[5])
    while count>0:
        t=count
        for r4 in answer[t]:
            for 
        
        count-=1
    print(len(answer))
    print(answer[6])
part2(tree,start)
        
        
            
    