import sys

deque = []
count  = 0
command_num = int(sys.stdin.readline())
while True:
    if count == command_num:
        break
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        new_deque = [int(command[1])]
        for i in deque:
            new_deque.append(i)
        deque = new_deque
    elif command[0] =="push_back":
        deque.append(int(command[1]))
    elif command[0] =="pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            if len(deque) == 1:
                deque = []
            else:
                deque = deque[1:]
    elif command[0] =="pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            if len(deque) == 1:
                deque = []
            else:
                deque = deque[:-1]
    elif command[0] =="size":
        print(len(deque))
    elif command[0] =="empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] =="front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif command[0] =="back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    count = count + 1

    
        
        


