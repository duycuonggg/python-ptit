T = int(input())
while T > 0:
  T -= 1
  # N: tiền gửi, X: phần % lãi, M: số tiền đạt được sau số năm
  N, X, M = map(float, input().split())
  years = 0 
  while N < M:
    N *= (1 + X/100)
    years += 1
  print(years)