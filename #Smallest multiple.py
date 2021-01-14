#Smallest multiple
import math
type(math.inf)

for i in range (1, 21):
    for e in range (1, math.inf):
        if e%i == 0:
            print (e)
