T = int(input())
while T > 0:
  N = input()
  # all() trả về True khi tất cả dữ kiện đúng
  # duyệt ch trong N xong kiểm tra ch có nằm trong chuỗi 47 không
  if all(ch in '47' for ch in N):
    print('YES')
  else:
    print('NO')
  T -= 1