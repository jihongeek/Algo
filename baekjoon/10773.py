import sys

stack = []
k = int(sys.stdin.readline().strip())

for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stack.pop() 
    else:
        stack.append(num)

print(sum(stack))