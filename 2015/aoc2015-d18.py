#848 to low

import copy
def nextseat(seating,px,py,x,y):
    if px+x<0 or py+y<0:
        return False
    try:
        if seating[py+y][px+x] == "#":
            return True
        elif seating[py+y][px+x] == ".":
            return False
#             return nextseat(seating,px+x,py+y,x,y)
    except:
        return False
                        
def checkoccupied(seating,posx,posy):
    counting=0
    if nextseat(seating,posx,posy,-1,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,0,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,-1,0):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,0):
        counting = counting + 1
    if nextseat(seating,posx,posy,-1,1):
        counting = counting + 1
    if  nextseat(seating,posx,posy,0,1):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,1):
        counting = counting + 1
    if counting == 3 or counting == 2:
        return False
    return True
def checkempty(seating,posx,posy):
    counting=0
    if nextseat(seating,posx,posy,-1,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,0,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,-1):
        counting = counting + 1
    if nextseat(seating,posx,posy,-1,0):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,0):
        counting = counting + 1
    if nextseat(seating,posx,posy,-1,1):
        counting = counting + 1
    if  nextseat(seating,posx,posy,0,1):
        counting = counting + 1
    if nextseat(seating,posx,posy,1,1):
        counting = counting + 1
    if counting == 3:
        return True
    return False
seat = []
with open ("/Users/Adam/aoc2015-d19.txt") as seats:
    for each in seats:
        seat.append(list(each.strip()))

newlist = []
seat[0][0]="#"
seat[0][len(seat[0])-1]="#"
seat[len(seat)-1][0]="#"
seat[len(seat)-1][len(seat[0])-1]="#"
for q in range(100):
    newlist=copy.deepcopy(seat)
    
    for i in range(len(seat)):
        for t in range(len(seat[0])):
            if seat[i][t] == "." and checkempty(newlist,t,i):
                seat[i][t]="#"
            elif seat[i][t] == "#" and checkoccupied(newlist,t,i):
                seat[i][t]="."
    seat[0][0]="#"
    seat[0][len(seat[0])-1]="#"
    seat[len(seat)-1][0]="#"
    seat[len(seat)-1][len(seat[0])-1]="#"
            
    
count = 0
for i in range(len(seat)):
    for t in range(len(seat[0])):
        if seat[i][t]=="#":
            count = count + 1
            
print(count)
