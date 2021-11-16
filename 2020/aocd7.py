
  
# function to get unique values 
def num_bag(bags):
    total = 1
    for rules in bagrules:
        if str(bags) in rules[:rules.find(":")]:
            temp=rules[rules.find(" :")+2:]
            temp1=temp.split(",")
            if "no other" in rules:
                return int(1)
            for each in temp1:
                each = each.split(" ",2)
                total = total + int(each[1])*num_bag(each[2][:each[2].rfind(" ")])       
    
    return total
    
    
bagrules=[]
with open("/Users/Adam/Desktop/aocd7.txt",newline="") as bags:
    for line in bags:
        bagrules.append(line.replace("contain",":").rstrip())
exbag = ["shiny gold"]

#for each in exbag:
#    for bag in bagrules:
 #       if each in bag[bag.find(":"):bag.rfind(" bag")] and bag[:bag.find(" :")] not in exbag:
#            exbag.append(bag[:bag.find(" bag")].strip())
#tempbag = []
#for each in exbag:
#    if each not in tempbag:
#        tempbag.append(each)
#print(len(tempbag))
#print(len(exbag))

inbag = "shiny gold"


print(num_bag(inbag))
        
        