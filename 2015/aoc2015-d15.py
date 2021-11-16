cookies=[[5,-1,0,0,5],[-1,3,0,0,1],[0,-1,4,0,1],[-1,0,0,8]]
x=0#cap
y=0#dur
u=0#flav
t=0#text
cal=0
maxi=0
total=100
for i in range(101): #number of sprinkles
    for b in range(101-i): #PB
        for c in range(101-i-b): #Frosting
            for d in range(101-i-b-c): #sugar
                if i+b+c+d==100:
                    x=i*5+b*-1+d*-1
                    y=i*-1+b*3+c*-1
                    u=i*0+b*0+c*4+d*0
                    t=i*0+b*0+c*0+d*2
                    if x<0:x=0
                    if y<0:y=0
                    if u<0:u=0
                    if t<0:t=0
                    cal = i*5+b+c*6+d*8
                    if x*t*u*y>maxi and cal==500:
                        maxi=x*t*u*y
print(maxi)
    