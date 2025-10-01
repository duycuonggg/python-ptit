# [2:] bỏ 2 kí tự đầu
for t in range(int(input())):
  b = int(input())
  x = input().strip()
  # đổi hệ nhị phân thành số nguyên
  num = int(x, 2)
  if b == 2:
    # chuyển chuỗi nhị phân cơ số 2
    print(bin(num)[2:])
  # vì cơ số 4 không hỗ trợ chuyển nên làm thủ công
  elif b == 4:
    ans = ''
    while num > 0:
      # lấy số dư chia cho 4 chuyển về chuỗi và ghép vào đầu
      ans = str(num % 4) + ans
      # chia nguyên cho 4 đề giảm dần
      num //= 4
    # nếu kết quả có thì in ra không thì in ra 0
    print(ans if ans else '0')
  # chuyển chuỗi nhị phân cơ số 8
  elif b == 8:
    print(oct(num)[2:])
  # chuyển chuỗi nhị phân cơ số 16
  elif b == 16:
    print(hex(num)[2:].upper())