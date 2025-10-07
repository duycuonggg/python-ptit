import math

n, k = list(map(int, input().split()))
result = []
for i in range(10**(k-1), 10**k):
  if math.gcd(i, n) == 1:
    result.append(i)
for i in range(0, len(result), 10):
  print(' '.join(map(str, result[i:i+10])))