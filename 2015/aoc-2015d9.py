
citiesdis = [[0,65,129,144,71,137,3,149],
          [65,0,63,4,105,125,55,14],
          [129,63,0,68,52,65,22,143],
          [144,4,68,0,8,23,136,115],
          [71,105,52,8,0,101,84,96],
          [137,125,65,23,101,0,107,14],
          [3,55,22,136,84,107,0,46],
          [149,14,143,115,96,14,46,0]]
cities="01234567"
def genlist(path,build,city):
    if(len(city)==0):
        return build
    for i in range(len(city)):
        if i == 0:
            temp = city[i+1:]
        elif i == len(city)-1:
            temp = city[:i]
        else:
            temp = city[:i] + city[i+1:]
        path.append(genlist(path,build+city[i],temp))
    return path
mini = 9999999
maxi = 0
paths=genlist([],"",cities)
path=[]
for each in paths:
    if len(each)==8:
        path.append(each)
for each in path:
    dis=0
    for i in range(len(each)-1):
        dis+=citiesdis[int(each[i])][int(each[i+1])]
    if dis>maxi:
        maxi=dis
    if dis<mini:
        mini=dis
        
print("mini " + str(mini) +"\nMax " + str(maxi))



