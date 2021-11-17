##this an ability score roller
import random
def roll(s):
  return random.randint(1,s)
def abilityscore():
    total=low=temp=roll(6)
    print(total)
    for t in range(1,4,1):
        temp=roll(6)
        if temp<low:
            low=temp
        total+=temp
    return total-low
print(abilityscore())
