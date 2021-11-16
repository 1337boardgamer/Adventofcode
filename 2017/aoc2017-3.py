#too  high 531441
temp=[]
array=[]
import math
import copy
import time
for t in range(100):
    temp.append(0)
for t in range(100):
    array.append(copy.deepcopy(temp))
def part1(a):
    arrs = 515
    coor=[arrs/2,arrs/2]
    count=1
    total=1
    size=8
    while total<265149:
        count+=1
        total+=size
        size+=8
    total=total-265149
    print(257-total+257)
    print(abs(total-arrs)+count)
#part1(a)
def part2(a):
    sizes=50
    coors=[sizes,sizes]
    
    ring=1
    size=8
    count=1
    a[coors[0]][coors[1]]=1
    temp=int(math.sqrt(ring))
    while a[coors[0]][coors[1]]<265149 and ring:
        temp=int(math.sqrt(ring))
        count=0
        coors[0]+=1
        while count<size:
                    count+=1
                    try:
                        a[coors[0]][coors[1]]=a[coors[0]-1][coors[1]-1]+a[coors[0]-1][coors[1]]+a[coors[0]-1][coors[1]+1]+a[coors[0]][coors[1]-1]+a[coors[0]][coors[1]+1]+a[coors[0]+1][coors[1]-1]+a[coors[0]+1][coors[1]]+a[coors[0]+1][coors[1]+1]
                        if a[coors[0]][coors[1]] >= 265149:
                            print(a[coors[0]][coors[1]])
                    except:
                        pass
                    print(a[coors[0]][coors[1]])
                    if coors[0]-sizes==ring and coors[1]-sizes>-ring and count<size:
                        coors[1]-=1
                    elif coors[0]-sizes>-ring and coors[1]-sizes==-ring:
                        coors[0]-=1
                    elif coors[0]-sizes==-ring and coors[1]-sizes<ring:
                        coors[1]+=1
                    elif coors[0]-sizes<ring and coors[1]-sizes==ring:
                        coors[0]+=1
                    time.sleep(.5)
                        
        size+=8
        ring+=1

    return a
print(part2(array))