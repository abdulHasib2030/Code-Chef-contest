for _ in range(int(input())):
  lst= list(map(str, input().split()))

  cnt = 0
  flag = False
  for i in range(6):
    if lst[i] == 'W':
      cnt += 1
    else:
      cnt = 0
    if cnt == 3:
      flag = True
      break
  if flag:
    print("YES")
  else:
    print("NO")