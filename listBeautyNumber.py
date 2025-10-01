def palindrome(s):
  # nếu độ dài dư 1 hoặc 2 số đầu cuối khác nhau thì sai
  if len(s) % 2 == 1 or s != s[::-1]:
    return False
  for i in s:
    # số trong mảng lẻ thì sai
    if int(i) % 2 == 1:
      return False
  return True

for t in range(int(input())):
  n = int(input())
  # vòng lặp từ 22 đến n bước nhảy 2 vì chỉ có các số 02468
  for i in range(22, n, 2):
    if palindrome(str(i)):
      print(i, end=' ')
  print()