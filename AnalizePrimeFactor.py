# sử dụng thuật toán chia thử (algorithm trial division)
import math

def primeFactor(n):
  factors = []
  for i in range(2, math.isqrt(n) + 1):
    count = 0
    while n % i == 0:
      n //= i
      count += 1
      # nếu count > 0 thì thêm vào chuỗi 
    if count > 0:
      # append nhận 1 đối số nếu muốn hơn cho vào ()
      factors.append((i, count))
    # nếu n không chia hết cho i và > 1 thì là số nguyên tố cuối cùng
  if n > 1:
    factors.append((n, 1))
  return factors
for t in range(int(input())):
  n = int(input())
  factors = primeFactor(n)
  result = ['1']
  for a, b in factors:
    result.append(f'{a}^{b}')
  print(' * '.join(result))