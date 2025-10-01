import math

def sumGcd(x, y):
  # tính ước số chung lớn nhất của 2 số
  gcdTwoNumber = math.gcd(x, y)
  # tính tổng ước số chung
  totalGcdTwoNumber = sum(int(d) for d in str(gcdTwoNumber))
  return totalGcdTwoNumber

# tính số nguyên tố
def isPrime(n):
  if n < 2: return False
  for i in range(2, math.isqrt(n) + 1):
    if n % i == 0: return False
  return True

for t in range(int(input())):
  a, b = map(int, input().split( ))
  if isPrime(sumGcd(a, b)):
    print('YES')
  else:
    print('NO')


