import math

for t in range(int(input())):
  n = int(input())
  if math.gcd(n, int(str(n)[::-1])) == 1: print('YES')
  else: print('NO')