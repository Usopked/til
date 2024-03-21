num = int(input())
stack = []
for i in range(num):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
    print(stack)
print(sum(stack))