class password:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    def check(self):
        checking = False
        for q in range(len(self.password)-1):
            try:
                if self.password[q] == self.password[q+1]-1 == self.password[q+2]-2:
                    checking=True
            except:
                pass
        for q in range(len(self.password)-1):
            if self.password[q] == 8 or self.password[q] == 11 or self.password[q] == 14:
                checking = False
                break
        dcheck = 0
        for q in range(len(self.password)-1):
            if self.password[q]==self.password[q+1]:
                dcheck += 1
                q += 1
        if dcheck <2:
            checking = False
        if checking:
            self.true=False
        
    
    def charcheck(self):
        if self.password[0]==26:
            self.true = False
        for i in range(len(self.password),0):
            if self.password[i] ==26:
                self.password[i] =0
                self.password[i-1]+=1
    def genpass(self):
        while self.true:
            self.password[len(self.password)-1]+=1
            self.charcheck()       
            for i in range(self.password[len(self.password)-1],25):
                self.password[len(self.password)-1]=i
                self.check()
                if self.true:
                    pass
                else:
                    break
    def __init__(self,passw):
        self.password = passw
        self.depth = 1
        self.true=True
    def __str__(self):
        print(self.password)
pas = password([2,16,9,23,9,13,3,18])
#pas= password([1,1,2,3,2])
pas.genpass()
for each in pas.password:
    print(pas.alpha[each])