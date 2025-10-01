import re

for t in range(int(input())):
  s = input().strip()
  numbers = re.findall(r'\d+', s)
  numbers = list(map(int, numbers))
  print(max(numbers))