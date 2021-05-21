t = int(input())
for _ in range(t):
  a = int(input())
  d = [0]*(a+1)
  d[0] = 1
  for L in range(1, a+1):
    for i in range(2,(a+1)):
        d[L] += (d[i-2] * d[L-i])
        d[L] %= 1000000007
  print(d[a])
