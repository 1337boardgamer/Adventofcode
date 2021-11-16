
count=0
group=0
customsgroup = []
customsgroup.append([])
with open("/Users/Adam/Desktop/aocd6.txt",newline="") as customs:
    for line in customs:
        if line =="\n":
            group = group + 1
            customsgroup.append([""])
        else:
            customsgroup[group].append(line.rstrip())
for i in range(len(customsgroup)):
    filter(None,customsgroup[i])
for group in customsgroup:
    for teach in group:
        tempstr=teach
    for each in group:
        for t in tempstr:
            if t in each or each == "":
               pass
            else:
                tempstr=tempstr.replace(t,'')
    print(tempstr)                                   
    count = count + len(tempstr)
print(count)