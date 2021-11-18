#611 to low
#1000 to high
#920 wrong
import copy
class spells:
    def __init__(self,m):
        self.mana=m
        self.spentmana=0
        #poison timer
        self.ptimer=0
        #shield timer
        self.stimer=0
        #recharge timer
        self.rtimer=0
    #poison call
    def poisoncheck(self):
        if self.ptimer>0:
            self.ptimer-=1
            return -3
        else:
            return 0
    def shieldcheck(self):
        if self.stimer>0:
            self.stimer-=1
            return 7
        else:
            return 0
    def recharagecheck(self):
        if self.rtimer>0:
            self.rtimer-=1
            self.mana+=110
        else:
            return 0
    #spell Casting
    def poisoncast(self):
        self.ptimer=6
        self.mana-=173
        self.spentmana+=173
    def shieldcast(self):
        self.stimer=6
        self.mana-=113
        self.spentmana+=113
    def rechargecast(self):
        self.rtimer=5
        self.mana-=229
        self.spentmana+=229
    def draincast(self):
        self.mana-=73
        self.spentmana+=73
        return 2
    def magicmissle(self):
        self.mana-=53
        self.spentmana+=53
        return 4
    def manacheck(self):
        if self.mana<0:
            return False
        return True
class player:
    #player HP, mana, armor, spent mana
    def __init__(self,h=50,m=500,a=0):
        self.hp=h
        self.mana=m
        self.armor=a
        self.playerspells = spells(self.mana)
class boss:
    #boss hp, attack
    def __init__(self):
        self.hp=55
        self.attack=8
def part1(b,p):
    pass
def test(b,p):
    attack=""
    
    
b=boss()
p=player(10,250)
print(p.mana)
part1(b,p)
            

