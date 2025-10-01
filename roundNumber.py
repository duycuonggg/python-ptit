def round_number(n):
  # nếu n <= 10 thì trả về n
  if n <= 10:
    return n
  number = 1
  while True:
    # vd: n = 99 -> ((99 + 10^1 // 2) // 10^1) * 10^1 -> (104 // 10^1) * 10^1 -> 10 * 10^1 -> 100
    custom = 10 ** number
    n = ((n + custom // 2) // custom) * custom
    # nếu n < đơn vị tiếp theo thì trả về n
    if n < custom * 10:
      return n
    number += 1

cases = int(input())
for _ in range(cases):
  n = int(input())
  result = round_number(n)
  print(result)