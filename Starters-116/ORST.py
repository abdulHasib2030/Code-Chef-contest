for _ in range(int(input())):
  a, b = map(int, input().split())
  lst = list(map(int, input().split()))
  lst2 = list(map(int, input().split()))
  
  for i in lst2:
    lst[-i:] = sorted(lst[-i:])
  print(*lst)
  