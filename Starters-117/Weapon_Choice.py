import math
for _ in range(int(input())):
  h, x, y1, y2, k = map(int, input().split())
  minn = h / x
  minn = math.ceil(minn)
  ans = y1 * k
  if ans >= h:
    ans -= h
    ans //= y1
    
    minn = min(minn, k - ans)
  elif ans < h:
    ans = h- ans
    ans /= y2
    ans = math.ceil(ans)
    minn = min(minn, k + ans)
  print(minn) 
    