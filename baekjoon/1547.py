from sys import stdin 

"""
    전략
        크기 3인 배열을 만들고, 공을 0번 칸에 넣고
        입력이 들어오면 배열의 요소를 바꾼다.  
"""

m = int(stdin.readline().strip())
cups = [True] + [False]*2
for _ in range(m):
    a,b = map(int, stdin.readline().strip().split())
    cups[a-1],cups[b-1] = cups[b-1],cups[a-1]
for i in range(3):
    if cups[i]:
        print(i+1)