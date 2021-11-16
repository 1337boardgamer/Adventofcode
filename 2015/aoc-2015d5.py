import re

reg = r"([a-z][a-z])[a-z]*\1"
reg1 = r"([a-z]).\1"
nice =0

with open ("/Users/Adam/aoc-2015d5.txt") as file:
    for each in file:
        t=re.search(reg,each)
        y=re.search(reg1,each)
        try:
            t.group()
            y.group()
            nice += 1
        except:
            pass
print(nice)