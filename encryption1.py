for t in range(int(input())):
  s = input().strip()
  res = []
  count = 1
  for i in range(1, len(s)):
    # nếu 2 kí tự bằng nhau + thêm 1
    if s[i] == s[i - 1]:
      count += 1
    else:
      # nếu khác thì giữ nguyên chuỗi và chuyển count về 1
      res.append(str(count) + s[i - 1])
      count = 1
  # do kết thúc vòng lặp không còn kí tự nào để báo kết thúc vòng lặp nên sẽ không được thêm vào nên phải thêm chuỗi cuối vào
  res.append(str(count) + s[-1])
  print(''.join(res))