for t in range(int(input())):
  p, q = input().split()
  a = input().split()
  # nếu chuỗi chỉ có 1 thì xuống dòng không thì in trên 1 dòng
  if len(a) == 1:
    x1 = a[0]
    x2 = input()
  else: 
    x1, x2 = a
  num1 = int(x1.replace(p, q)) + int(x2.replace(p, q))
  num2 = int(x1.replace(q, p)) + int(x2.replace(q, p))
  print(min(num1, num2), max(num1, num2))