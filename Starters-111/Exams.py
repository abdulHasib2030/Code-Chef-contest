for _ in range(int(input())):
  x, y, z = map(int, input().split())
  if (x * y)//2 < z:
    print('YES')
  else:
    print('NO') 