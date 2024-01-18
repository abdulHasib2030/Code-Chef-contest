# cook your dish here
import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    else:
        diff = abs(a -b)
        e = -1
        sq = int(math.sqrt(diff* 2))
        for i in range(sq, sq+6):
            temp = (i *(i+1)) // 2
            d = temp - diff
            
            if d < 0:
                continue
            if d % 2 == 0:
                e = i
                break
        print(e)
        
        