from sys import stdin
from collections import deque
for testcase in range(int(stdin.readline().strip())):
    n,m = map(int,stdin.readline().strip().split())
    inputList = list(map(int,stdin.readline().strip().split()))
    inputList = [(x,i) for i,x in enumerate(inputList)]
    
    toPrint = []
    queue1 = deque(inputList)
    queue2 = deque()
    for i in  range(n):
        now = queue1.popleft()
        while len(queue1) > 0:
            front = queue1.popleft()
            if front[0] > now[0]:
                queue1.append(now)
                now = front
                while len(queue2) > 0:
                    queue1.append(queue2.popleft())
            else:
                queue2.append(front)
        while len(queue2) > 0:
            queue1.append(queue2.popleft())
        toPrint.append(now)
        
    for i,doc in enumerate(toPrint):
        if doc[1] == m:
            print(i+1)
            break         
    
