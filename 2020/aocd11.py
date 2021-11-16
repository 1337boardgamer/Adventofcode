import copy
def nextseat(seating,px,py,x,y):
    if px+x<0 or py+y<0:
        return False
    try:
        if seating[py+y][px+x] == "#":
            return True
        elif seating[py+y][px+x] == "L":
            return False
        elif seating[py+y][px+x] == ".":
            return nextseat(seating,px+x,py+y,x,y)
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
    if counting >= 5:
        return True
    return False
def checkempty(seating,posx,posy):
    if nextseat(seating,posx,posy,-1,-1):
        return False
    if nextseat(seating,posx,posy,0,-1):
        return False
    if nextseat(seating,posx,posy,1,-1):
        return False
    if nextseat(seating,posx,posy,-1,0):
        return False
    if nextseat(seating,posx,posy,1,0):
        return False
    if nextseat(seating,posx,posy,-1,1):
        return False
    if  nextseat(seating,posx,posy,0,1):
        return False
    if nextseat(seating,posx,posy,1,1):
        return False
    return True
seat = []
with open ("/Users/Adam/Desktop/aocd11.txt") as seats:
    for each in seats:
        seat.append(list(each.strip()))
newlist = []
while newlist!=seat:
    newlist=copy.deepcopy(seat)
    for i in range(len(seat)):
        for t in range(len(seat[0])):
            if seat[i][t] == "L" and checkempty(newlist,t,i):
                seat[i][t]="#"
            elif seat[i][t] == "#" and checkoccupied(newlist,t,i):
                seat[i][t]="L"
            
    
count = 0
for i in range(len(seat)):
    for t in range(len(seat[0])):
        if seat[i][t]=="#":
            count = count + 1
            
print(count)
