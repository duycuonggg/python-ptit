n = int(input())
a = list(map(int, input().split()))
stack = []
for i in a:
  # kiểm tra mảng không rỗng và 2 vị trí liền kề cộng lại không chẵn
  if stack and (stack[-1] + i) % 2 == 0: stack.pop()
  else: stack.append(i)
print(len(stack))