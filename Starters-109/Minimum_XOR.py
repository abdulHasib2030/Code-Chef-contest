
for _ in range(int(input())):
  n = int(input())
  test_cases = list(map(int, input().split()))
  xor_all = 0
  for i in test_cases:
    xor_all ^= i
  ans = xor_all
  for i in test_cases:
    tem = xor_all ^ i
    ans = min(ans, tem)
  print(ans)
