for _ in range(int(input())):
  n, x = map(int, input().split())
  s = input()
  temp  = x
  flag = 0
  if s[0] == '0':
    print("NO")
    continue
  
  for i in range(n):
    if s[i] == '0':
      temp -= 1
    else:
      temp = max(temp, x)
    if temp < 0:
      flag = 1
      break
  if flag == 1:
    print("NO")
  else:
    print("YES")
    