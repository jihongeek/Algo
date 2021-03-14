import sys

stack = []
count  = 0
command_num = int(sys.stdin.readline())
while True:
    if count == command_num:
        break
    command = sys.stdin.readline().split()
    if command[0] =="push":
        stack.append(int(command[1]))
    elif command[0] =="pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            if len(stack) == 1:
                stack = []
            else:
                stack = stack[:-1]
    elif command[0] =="size":
        print(len(stack))
    elif command[0] =="empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] =="top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    count = count + 1

    
        
        


