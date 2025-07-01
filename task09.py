#9. Sonlar nechta raqamdan iboratligini (1 xonali, 2 xonali...) aniqlang.

import math 

with open("Input/numbers.txt") as number:
    numbers = number.read().split()
    n = list(map(int,numbers))
    
    jami = {}
    
    for son in n:
        uzunlik = len(str(abs(son)))
         
        if uzunlik not in jami:
            jami[uzunlik] = 1
        else:
            jami[uzunlik] += 1
    
with open("Output/output09.txt","w") as num:
    for xona,soni in sorted(jami.items()):
        num.write(f"{xona} xonali sonlar {soni} ta\n")