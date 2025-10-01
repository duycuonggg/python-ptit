for t in range(int(input())):
  s = input().strip()
  res = []
  # bước nhảy 2
  for i in range(0, len(s) - 1, 2):
      char = s[i]
      # kí tự 2 ép kiểu nguyên
      count = int(s[i + 1])
      res += char * count
  # res là mảng nếu *res sẽ có cách nên dùng join
  print(''.join(res))