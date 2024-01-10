for _ in range(int(input())):
  n = int(input())
  lst = []
  for i in range(1,n+1, 2):
    lst.append(i)
  k = len(lst)
  cnt = 0
  j = k-1
  for i in range((k // 2)):
    st = ""
    if lst[i] + lst[j] == n:
      st += str(lst[i])
      st += str(lst[j])
      flag = True
      for i in range(1, len(st)):
        if st[i] == st[i-1]:
          flag = False
      if flag:
        cnt += 1
        
    j-=1
    

  print(cnt)
