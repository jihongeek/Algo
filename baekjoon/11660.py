from sys import stdin 
"""

    표에 대응되는 행 한 줄씩 누적합을 저장하고,
    x1 ~ x2, y1 ~ y2 범위에 따라 누적합울 이용해서 숫자들의 합을 계산한다.
    ->  arr[row][y2] - arr[row][y1-1] + arr[row][y2] - arr[row][y1-1] ...
"""
n,m = map(int,stdin.readline().strip().split())
sum_table = [[0]*(n+1)]
for _ in range(n):
    temp_line = list(map(int,stdin.readline().strip().split()))
    # 누적합 표 만들기
    sum_line = [0,temp_line[0]]
    for i in range(2,n+1):
        sum_line.append(sum_line[i-1] + temp_line[i-1])
    sum_table.append(sum_line)

for _ in range(m):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    answer = 0
    # 범위에 따라 주어진 범위에 해당되는 숫자들의 합을 한 줄씩 더해가며 구한다. 
    for row in range(x1,x2+1):
        answer += (sum_table[row][y2] - sum_table[row][y1-1])
    print(answer)
    
