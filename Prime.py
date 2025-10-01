import math

# kiểm tra 2 số nguyên tố có ước chung lớn nhất = 1
def isCoprime (x, y):
  if (math.gcd(x, y) == 1):
    return True
  return False

# kiểm tra số nguyên tố (số nguyên tố là số chia hết cho 1 và chính nó)
def isPrime (n):
  if n < 2: return False
  for i in range (2, math.isqrt(n) + 1):
    if n % i == 0: return False
  return True

T = int(input())
while T > 0:
  T -= 1
  N = int(input())
  count = 0
  for i in range(1, N):
    if isCoprime(N, i):
      count += 1
  if isPrime(count):
    print('YES')
  else:
    print('NO')
