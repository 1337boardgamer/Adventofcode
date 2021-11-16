
citiesdis = [[0,54,-81,-42,89,-89,97,94,0],
          [3,0,-70,-31,72,-25,-95,11,0],
          [-83,8,0,35,10,61,10,29,0],
          [67,25,48,0,-65,8,84,9,0],
          [-51,-39,84,-98,0,-20,-6,60,0],
          [51,79,88,33,43,0,77,-3,0],
          [-14,-12,-52,14,-62,-18,0,-17,0],
          [-36,76,-34,37,40,18,7,0,0],
          [0,0,0,0,0,0,0,0,0]]
cities="012345678"
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
maxi = -10000000
paths=genlist([],"",cities)
path=[]
for each in paths:
    if len(each)==9:
        path.append(each)
for each in path:
    dis=0
    for i in range(len(each)):
        if i==0:
            dis += citiesdis[int(each[i])][int(each[i+1])]+citiesdis[int(each[i])][int(each[8])]
        elif i==8:
            dis += citiesdis[int(each[i])][int(each[i-1])]+citiesdis[int(each[i])][int(each[0])]
        else:
            dis += citiesdis[int(each[i])][int(each[i-1])]+citiesdis[int(each[i])][int(each[i+1])]
    if dis>maxi:
        maxi=dis
    if dis<mini:
        mini=dis
        
        
print(mini)
print(maxi)