import hashlib



def hashs (secret):
    i=0
    while 1:
        trying = secret + str(i)
        trying = hashlib.md5(trying.encode())
        if str(trying.hexdigest())[:6]=="000000":
            return i
        i += 1
        
print(str(hashlib.md5("trtyreasdasdasdaasd".encode()))[:6])
print(hashs("iwrupvqb"))
