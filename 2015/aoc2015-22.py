import copy
#611 to low
#1000 to high
#920 wrong
def check(cast):
    if len(cast)< 4:
        return cast
    else:
        mana=500
        sm=0
        ph=50
        b=55
        pa=0
        s=0
        p=0
        r=0
        t=0
        for w in range(len(cast)):
            if s==0:
                pa=0
            if s>0:
                pa=7
                s-=1
            if p>0:
                b-=3
                p-=1
            if r>0:
                mana+=101
                r-=1
            if b<1:
                b=0
                t=w
                return cast[:t]
                break
            if cast[w]=="m" and mana-53>=0:
                mana-=53
                sm+=53
                b-=4
            elif cast[w]=="d" and mana-73>=0:
                mana-=73
                sm+=73
                b-=2
                ph+=2
            elif cast[w]=="s" and mana-113>=0:
                mana-=113
                sm+=113
                s=6
            elif cast[w]=="p" and mana-173>=0:
                mana-=173
                sm+=173
                p=6
            elif cast[w]=="r" and mana-229>=0:
                mana-=229
                sm+=229
                r=5
            else:
                ph=0
                return ""
                break
            if s==0:
                pa=0
            if s>0:
                pa=7
                s-=1
            if p>0:
                b-=3
                p-=1
            if r>0:
                mana+=101
                r-=1
            if b>0:
                ph-=(8-pa)
            if sm>973:
                ph=0
                return ""
                break
            if mana<0:
                ph=0
                return ""
                break
            if b<1:
                b=0
                t=w
                return cast[:t]
                break
                
        if ph==0:
            return ""
        elif b==0:
            return cast[:t]
        else:
            return cast

def fight(cast):
    mana=500
    sm=0
    ph=50
    b=55
    pa=0
    s=0
    p=0
    r=0
    
    for w in cast:
        if s==0:
            pa=0
        if s>0:
            pa=7
            s-=1
        if p>0:
            b-=3
            p-=1
        if r>0:
            mana+=101
            r-=1
        if b<1 and ph>0:
            return sm
        if w=="m" and mana-53>=0:
            mana-=53
            sm+=53
            b-=4
        elif w=="d" and mana-73>=0:
            mana-=73
            sm+=73
            b-=2
            ph+=2
        elif w=="s" and mana-113>=0:
            mana-=113
            sm+=113
            s=6
        elif w=="p" and mana-173>=0:
            mana-=173
            sm+=173
            p=6
        elif w=="r" and mana-229>=0:
            mana-=229
            sm+=229
            r=5
        else:
            p=0
            return 10000
            break
        if s==0:
            pa=0
        if s>0:
            pa=7
            s-=1
        if p>0:
            b-=3
            p-=1
        if r>0:
            mana+=101
            r-=1
        if b>0:
            ph-=(8-pa)
        if sm>973:
            ph=0
            return 10000
            break
        if mana<0:
            ph=0
            return 10000
            break
        if b<1 and ph>0:
            return sm
    return 10000
def fighttest(cast):
    mana=250
    sm=0
    ph=10
    b=13
    pa=0
    s=0
    p=0
    r=0
    
    for w in cast:
        if s==0:
            pa=0
        if s>0:
            pa=7
            s-=1
        if p>0:
            b-=3
            p-=1
        if r>0:
            mana+=101
            r-=1
        if b<1 and ph>0:
            return sm
        if w=="m" and mana-53>=0:
            mana-=53
            sm+=53
            b-=4
        elif w=="d" and mana-73>=0:
            mana-=73
            sm+=73
            b-=2
            ph+=2
        elif w=="s" and mana-113>=0:
            mana-=113
            sm+=113
            s=6
        elif w=="p" and mana-173>=0:
            mana-=173
            sm+=173
            p=6
        elif w=="r" and mana-229>=0:
            mana-=229
            sm+=229
            r=5
        else:
            p=0
            return 10000
            break
        if s==0:
            pa=0
        if s>0:
            pa=7
            s-=1
        if p>0:
            b-=3
            p-=1
        if r>0:
            mana+=101
            r-=1
        if b>0:
            ph-=(8-pa)
        if sm>973:
            ph=0
            return 10000
            break
        if mana<0:
            ph=0
            return 10000
            break
        if b<1 and ph>0:
            return sm
    return 10000


            
                
            
string="mdprs"
casts=["m","d","p","r","s"]
d=[]
print(fight("prmpmmm"))
for e in casts:
    for t in range(len(string)):
        d.append(e+string[t])
casts = copy.deepcopy(d)
for f in casts:
    print(fighttest(f))
    

spells = [["m",53],["d",73],["s",113],["p",173],["r",229]]
spelloptions =["m","d","s","p","r"]
for i in range(10):
    temp=[]
    for q in spelloptions:
        for t in spells:
            if check(q+t[0])=="":
                pass
            else:
                temp.append(check(q+t[0]))
    spelloptions=copy.deepcopy(set(temp))
    print(len(spelloptions))
#print(spelloptions)

           
#spelloptions=['mprmspmm', 'mprmspmmd', 'mprmpsmm', 'mprmpsmmd', 'mprsmpmm', 'mprsmpmmd', 'mprspmmm', 'mprspmmmd', 'mrpmspmm', 'mrpmspmmd', 'mrpsmpmm', 'mrpsmpmmd', 'srpmmpmm', 'srpmmpmmd', 'pmrmspmm', 'pmrmspmmd', 'pmrmpsmm', 'pmrmpsmmd', 'pmrsmpmm', 'pmrsmpmmd', 'pmrspmmm', 'pmrspmmmd', 'pmrpmsmm', 'pmrpmsmmd', 'pmrpsmmm', 'pmrpsmmmd', 'prmmspmm', 'prmmspmmd', 'prmmpsmm', 'prmmpsmmd', 'prmsmpmm', 'prmsmpmmd', 'prmspmmm', 'prmspmmmd', 'prmpmsmm', 'prmpmsmmd', 'prmpsmmm', 'prmpsmmmd', 'prsmmpmm', 'prsmmpmmd', 'prsmpmmm', 'prsmpmmmd', 'prspmmmm', 'prspmmmmd', 'rmpmspmm', 'rmpmspmmd', 'rmpsmpmm', 'rmpsmpmmd', 'rspmmpmm', 'rspmmpmmd', 'rpmmspmm', 'rpmmspmmd', 'rpmmpsmm', 'rpmmpsmmd', 'rpmsmpmm', 'rpmsmpmmd', 'rpmspmmm', 'rpmspmmmd', 'rpsmmpmm', 'rpsmmpmmd', 'rpsmpmmm', 'rpsmpmmmd
mini=[]
length=222
for t in spelloptions:
    if len(t)<length:
        length=len(t)
    if len(t)==7:
        print(t)
    mini.append(fight(t))
print(length)
print(fight("prmpmmm"))   


# while bhp>0 or php>0:
#     break
    