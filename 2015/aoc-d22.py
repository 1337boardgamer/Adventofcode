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
            return 3
        else:
            return 0
    def shieldcheck(self):
        if self.stimer>0:
            self.stimer-=1
            return 7
        else:
            return 0
    def rechargecheck(self):
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
    def magicmisslecast(self):
        self.mana-=53
        self.spentmana+=53
        return 4
    def manacheck(self,cast=0):
        if self.mana-cast<0:
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
    def __init__(self,h=55,a=8):
        self.hp=h
        self.attack=a
def part1(boss,player):
    if test(boss,player,"pm")=="Player Wins":
        return "return I win"
def test(b,p,attack):
    for t in attack:
        damage=0
        b.hp-=p.playerspells.poisoncheck()
        p.playerspells.rechargecheck()
        p.playerspells.shieldcheck()
        if t=="p":
            if p.playerspells.manacheck(173):
                p.playerspells.poisoncast()
            else:
                return "Not enough Mana to cast the spell!"
        elif t=="s":
            if p.playerspells.manacheck(113):
                p.playerspells.shieldcast()
            else:
                return "Not enough Mana to cast the spell!"
        elif t=="m":
            if p.playerspells.manacheck(53):
                damage=p.playerspells.magicmisslecast()
            else:
                return "Not enough Mana to cast the spell!"
        elif t=="d":
            if p.playerspells.manacheck(73):
                damage=p.playerspells.draincast()
                p.hp+=damage
            else:
                return "Not enough Mana to cast the spell!"
        elif t=="r":
            if p.playerspells.manacheck(229):
                p.playerspells.rechargecast()
            else:
                return "Not enough Mana to cast the spell!"
        b.hp-=damage
        b.hp-=p.playerspells.poisoncheck()
        if b.hp<1:
            return "Player Wins"
        p.playerspells.rechargecheck()
        p.hp-=(b.attack-p.playerspells.shieldcheck())
        if p.hp<1 and b.hp<1:
            return "Both Die"
        elif p.hp<1:
            return "Player Dies"
        elif b.hp<1:
           return "Player Wins"
        
    return "Both Alive"
        
b=boss(14)
p=player(10,250)

print(part1(b,p))

            

