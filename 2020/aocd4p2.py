import csv
import math
import string
def is_hex(s):
    return set(s).issubset(string.hexdigits)

count = 0
pp = [dict()]
pp[0]={}
with open("/Users/Adam/Desktop/aocd4.csv",newline="") as passport:
    for line in passport:
        if line == "\n":
            count = count + 1
            pp.append({})
        else:
            for word in line.split(" "):
                words=word.split(":")
                pp[count][words[0]]=words[1].rstrip()
count =0
for entry in pp:
    if entry.keys()>={"byr","iyr","eyr","hgt","hcl","ecl","pid",}:
        if int(entry["byr"])<=2002 and int(entry["byr"]) >=1920 and int(entry["iyr"])<=2020 and int(entry["iyr"]) >=2010 and int(entry["eyr"])<=2030 and int(entry["eyr"]) >= 2020:
            if entry["ecl"]=="amb" or entry["ecl"] == "blu"or entry["ecl"] =="brn"or entry["ecl"] =="gry"or entry["ecl"] =="grn"or entry["ecl"] =="hzl"or entry["ecl"] =="oth":
                if entry["pid"].isdigit() and len(entry["pid"])==9:
                    
                    if entry["hcl"][0]=="#" and is_hex(["hcl"][1:]):
                        if "cm" in entry["hgt"]:
                            if int(entry["hgt"][:len(entry["hgt"])-2]) >= 150 and int(entry["hgt"][:len(entry["hgt"])-2]) <= 193:
                                count = count + 1
                        elif "in" in entry["hgt"]:
                            if int(entry["hgt"][:len(entry["hgt"])-2]) >= 59 and int(entry["hgt"][:len(entry["hgt"])-2]) <= 76:
                                count = count + 1
                        
print(count)       
