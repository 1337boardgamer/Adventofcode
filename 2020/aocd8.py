import copy
def tryin (tempp,tmp):
    temppro = copy.deepcopy(tempp)
    if temppro[tmp][0] == "nop":
        temppro[tmp][0] = "jmp"
    elif temppro[tmp][0] == "jmp":
        temppro[tmp][0] = "nop"
        
    while tmp < len(temppro):
        tmpjump=1
        if temppro[tmp][0] == "nop":
            pass
        elif temppro[tmp][0] == "acc":
            pass
        elif temppro[tmp][0] == "jmp":
            tmpjump = int(temppro[tmp][1])
        elif temppro[tmp][0] == "ran":
            return False
        temppro[tmp][0] = "ran"
        tmp = tmp + tmpjump
    return True
    
    
program = []
with open("/Users/Adam/Desktop/aocd8.txt",newline="") as code:
    for line in code:
        program.append(str(line).strip().split(" "))
count = 0
acc = 0
solved = False
print(len(program))
while count < len(program):
    if program[count][0] == "nop" or program[count][0] == "jmp":
        
        if tryin(program,count) and not solved:
            solved = True
            if program[count][0] == "nop":
                program[count][0] = "jmp"
            else:
                program[count][0] = "nop"
    jump=1
    print(program[count])
    if program[count][0] == "nop":
        pass
    elif program[count][0] == "acc":
        acc = acc + int(program[count][1])
    elif program[count][0] == "jmp":
        jump = int(program[count][1])
    elif program[count][0] == "ran":
        count = len(program) + 100
        break
    program[count][0] = "ran"
    count = count + jump
print(acc)   

    
    