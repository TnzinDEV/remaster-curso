TabY=["A","B","C","D","E"]
TabX=[1,2,3,4,5]

a = "~"
b = "-"
n ="X"

import random
item1=random.choice(TabY)
item2=random.choice(TabX)

number=item1+item2
print(number)

for TabY in TabX:
    print(TabY) 