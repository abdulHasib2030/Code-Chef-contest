for _ in range(int(input())):
  n = int(input())
  s = input()
  ans = ""
  idx = 0
  for i in range(1,n):
    if ord(s[i]) < ord(s[i-1]):
      idx = i-1
      break  
    else:
      idx = i
  for i in range(n):
    if idx == i:
      continue
    else:
      ans += s[i]
  print(ans)