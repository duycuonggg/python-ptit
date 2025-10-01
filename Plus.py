s = input()
# split tách chuỗi
left, right = s.split('=')
# eval thực thi biểu thức dưới dạng chuỗi
if eval(left) ==  int(right):
  print('YES')
else: 
  print('NO')