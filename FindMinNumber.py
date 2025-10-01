# thư viện regex xử lí xâu
import re

for t in range(int(input())):
  n = input().strip()
  # r'\d+', n: loại bỏ chữ trong xâu 
  # findall: timef tất cả
  numbers = re.findall(r'\d+', n)
  numbers = list(map(int, numbers))
  print(min(numbers))