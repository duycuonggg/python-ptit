# chuỗi đảo ngược
def reverse(n):
  return int(str(n)[::-1])

for t in range(int(input())):
  n = int(input())
  # nếu n chia hết cho 7 thì trả về luôn
  if n % 7 == 0:
    print(n)
    continue
  found = False
  # nếu tổng n và n đảo ngược chia hết cho 7 và bước lặp không vượt 1000
  for _ in range(1000):
    n += reverse(n)
    if n % 7 == 0:
      print(n)
      found = True
      break
  # nếu không tìm thấy in ra -1
  if not found: print(-1)