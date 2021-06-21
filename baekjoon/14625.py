from sys import stdin
start = list(map(int,stdin.readline().strip().split()))
end = list(map(int,stdin.readline().strip().split()))
n = stdin.readline().strip()
count = 0
for h in range(start[0],end[0]+1):
    m_start = 0
    m_end = 60
    if h == start[0]:
        m_start = start[1]
    if h == end[0]:
        m_end = end[1]
    for m in range(m_start,m_end+1):
        if m == 60:
            continue
        if n in "%02d %02d"%(h,m):
            count+=1 
print(count)

