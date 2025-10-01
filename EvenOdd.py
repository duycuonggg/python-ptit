for t in range(int(input())):
  n = input().strip()
  digits = list(map(int, n))
  # list mới dùng được sum
  total = sum(digits)
  ok = True
  for i in range(1, len(digits)):
    if abs(digits[i] - digits[i-1]) != 2:
      ok =  False
      break
  if total % 10 == 0 and ok: print('YES')
  else: print('NO')
  
