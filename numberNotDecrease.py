for t in range(int(input())):
  s = input().strip()
  ok = True
  # duyệt từ đầu mảng đến cuối mảng
  for i in range(len(s) - 1):
    # vị trí thứ 1 mà lớn hơn vị trí thứ 2 thì trả về False
    if s[i] > s[i + 1]:
      ok = False
      break
  print('YES' if ok else 'NO')
      