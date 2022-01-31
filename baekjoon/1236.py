from sys import stdin
"""
    전략
        열과,행에 모두 경비원이 없는 경우에 
        경비원을 먼저 배치하면 
        최소로 경비원을 추가 할 수 있다.
"""
n,m = map(int,stdin.readline().strip().split())
castle = []
for _ in range(n):
    line = stdin.readline().strip()
    castle.append(line)
count = 0
row_securities = [False]*n
col_securities = [False]*m 

for row in range(n):
    for col in range(m):
        if castle[row][col] == "X":
            row_securities[row] = True
            col_securities[col] = True

for row in range(n):
    for col in range(m):
        if not row_securities[row] and not col_securities[col]:
            count += 1
            row_securities[row] = True
            col_securities[col] = True

for row in range(n):
    for col in range(m):
        if not row_securities[row]: 
            count += 1
            row_securities[row] = True
        elif not col_securities[col]:
            count += 1
            col_securities[col] = True

print(count)