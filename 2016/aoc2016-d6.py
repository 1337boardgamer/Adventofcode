code=[]
for t in range(8):
    code.append("")
with open ("/Users/adam/aoc2016-d6.txt") as file:
    for each in file:
        each=each.strip()
        for i in range(len(each)):
            code[i]+=each[i]

from collections import Counter
  
def find(input):
  
    # now create dictionary using counter method
    # which will have strings as key and their 
    # frequencies as value
    wc = Counter(input)
  
    # Finding maximum occurrence of a character 
        # and get the index of it.
    s = max(wc.values())
    print(wc)
    return wc.items()
def part1(c):
    y=""
    for t in c:
        find(t)
def part2(c):
    pass
print(part1(code))
            