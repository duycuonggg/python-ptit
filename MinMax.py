while True:
  t = int(input())
  if t == 0: 
    break
    s = []
    for _ in range(t):
      n = int(input())
      s.append(n)
    if min(s) == max(s): print('BANG NHAU')
    else: print(f'{min(s)} {max(s)}')