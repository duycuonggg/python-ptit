# strip bỏ khoảng trắng đầu cuối
N = input().strip()
count = N.count('4') + N.count('7')
if count in (4, 7):
  print('YES')
else:
  print('NO')