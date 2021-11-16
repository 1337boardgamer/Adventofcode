class ship:
    def __init__(self):
        self.x=0
        self.y=0
        self.facing=1
        self.waypoint=[10,1]
    def movement(self,instruct):
        if instruct[0] =="F":
            self.x += int(instruct[1:])*self.waypoint[0]
            self.y += int(instruct[1:])*self.waypoint[1]
        elif instruct[0]== "R":
            if int(instruct[1:])==90:
                self.swap()
                self.waypoint[1]*=-1
            elif int(instruct[1:])==180:
                self.waypoint[1]*=-1
                self.waypoint[0]*=-1
            else:
                self.swap()
                self.waypoint[0]*=-1
        elif instruct[0]=="L":
            if int(instruct[1:])==90:
                self.swap()
                self.waypoint[0]*=-1
            elif int(instruct[1:])==180:
                self.waypoint[1]*=-1
                self.waypoint[0]*=-1
            else:
                self.swap()
                self.waypoint[1]*=-1
        else:
            facevaluex,facevaluey=self.direction(instruct[0])
            self.waypoint[0] += int(instruct[1:])*facevaluex
            self.waypoint[1] += int(instruct[1:])*facevaluey
            self.check()
            
    def facingvalue(self):
        if self.facing==1:
            return [1,1]
        if self.facing==3:
            return [-1,-1]
        if self.facing==0:
            return [-1,1]
        if self.facing==2:
            return [1,-1]
        return [0,0]
    
    def direction(self,facing):
        if facing=="E":
            return [1,0]
        if facing=="W":
            return [-1,0]
        if facing=="N":
            return [0,1]
        if facing=="S":
            return [0,-1]
        return[0,0]
    
    def turn(self,deg):
        deg=abs((int(int(deg)/90)))
        for i in range(deg):
            self.swap()
        self.check()    
        facing=self.facingvalue()
        self.waypoint[0] = facing[0] *abs(self.waypoint[0])
        self.waypoint[1] = facing[1]*abs(self.waypoint[1])
        
    def swap(self):
        self.waypoint[0],self.waypoint[1]=self.waypoint[1],self.waypoint[0]

    
    def check(self):
        facing=self.facingvalue()
        if facing[0]*self.waypoint[0]<0:
            facing[0]=self.waypoint[0]/abs(self.waypoint[0])
        if facing[1]*self.waypoint[1]<0:
            facing[1]=self.waypoint[1]/abs(self.waypoint[1])
        if facing==[1,1]:
            self.facing=1
        elif facing==[1,-1]:
            self.facing=2
        elif facing==[-1,-1]:
            self.facing=3
        elif facing==[-1,1]:
            self.facing==0

ship = ship()
with open ("/Users/Adam/aocd12.txt") as dirs:
    for each in dirs:
        ship.movement(each.strip())
        
print(abs(ship.x)+abs(ship.y))
print(ship.waypoint)
print(ship.x,ship.y)