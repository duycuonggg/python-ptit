a, K, N = map(int, input().split())
res = []
# cho a + b = m
# tính bội số  của K đầu tiên  m > a  vì (b > 0)
start = ((a // K) + 1) * K
# từ bội số đầu tiên đến N bước nhảy là K
for m in range(start, N + 1, K):
  # có m -> b = m - a
  res.append(m - a)
  
if res:
  # * để bỏ hiện mảng
  print(*res)
else:
  print('-1')