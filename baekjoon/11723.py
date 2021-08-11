from sys import stdin 
m = int(stdin.readline().strip())
s = 0
for _ in range(m):
    operation = stdin.readline().strip().split()
    if operation[0] == "add":
        s = s | 1 << int(operation[1])-1
    elif operation[0] == "remove":
        s = s & ~(1 << (int(operation[1])-1))
    elif operation[0] == "check":
        if s & (1 << int(operation[1])-1) == 0:
            print(0)
        else:
            print(1)
    elif operation[0] == "toggle":
        if s & (1 << int(operation[1])-1) == 0:
            s = s | 1 << (int(operation[1])-1)
        else:
            s = s & ~(1 << (int(operation[1])-1))
    elif operation[0] == "all":
        s = int("1"*20,2)
    else:
        s = 0 

    
