import math
for _ in range(int(input())):
  a, b = map(int, input().split())
  ans = math.floor(a/(b+1))
  result = a - (ans * (b+1))
  print(result+ans)  
  