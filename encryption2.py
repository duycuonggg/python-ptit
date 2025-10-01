p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
  line = input().strip()
  # kết thúc khi k = 0
  if line == '0':
    break
  k, s = line.split()
  # chuyên k về kiểu int
  k = int(k)
  decode = ''
  for ch in s:
    idx = p.index(ch)
    newCh = p[(idx+k)%28]
    decode += newCh
  print(decode[::-1])
