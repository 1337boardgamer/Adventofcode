mem = 0
actual = 0
how =0
test = [r"\"\"",r"\"abc\"",r"\"abc\"abc\"",r'\"\x34\"qqqweweqwe']



def check(string):
    length=len(string)
    remove=0
    for i in range(len(string)-2):
        if string[i] == '\\' and string[i+1]=="\\":
            remove += 1
            string = string[:i]+".."+string[i+2:]
        elif string[i:i+1] =="\\" and string[i+1]=="\"":
            remove += 1
            string = string[:i]+".."+string[i+2:]
        #elif string[i:i+1]=="\\" and string[i+1]=="x":
            #remove += 3
            #string = string[:i]+".."+string[i+3:]
            
    return remove+2
def part2(string):
    return string.count("\\") + string.count('"') 
with open ("/Users/Adam/aoc-2015d8.csv") as strings:
    for each in strings:
        actual += len(each)
        mem += (len('u'+each))
        how += part2(each) +2
        
print (how)

