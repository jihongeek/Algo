import sys

queue = []
count  = 0
command_num = int(sys.stdin.readline())
while True:
    if count == command_num:
        break
    command = sys.stdin.readline().split()
    if command[0] =="push":
        queue.append(int(command[1]))
    elif command[0] =="pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            if len(queue) == 1:
                queue = []
            else:
                queue = queue[1:]
    elif command[0] =="size":
        print(len(queue))
    elif command[0] =="empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] =="front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] =="back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    count = count + 1