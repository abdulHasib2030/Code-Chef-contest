for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  lst2 = list(map(int, input().split()))
  nutrition = 0
  seen = set()
  dupes = [x for x in lst if x in seen or seen.add(x)] 
  dic = {}
  for i in seen:
    dic[i] = 0

  for i in range(n):
    if dic[lst[i]] < lst2[i]:
      nutrition = (nutrition - dic[lst[i]]) + lst2[i]
      dic[lst[i]] = lst2[i]
  print(nutrition)