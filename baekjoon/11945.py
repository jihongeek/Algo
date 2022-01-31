from sys import stdin 
"""
    전략
        입력되는 붕어빵의 줄마다 
        대칭되는 인덱스에 있는 정수를 출력하면된다.
"""
n,m = map(int, stdin.readline().strip().split())
for _ in range(n):
    line = stdin.readline().strip()
    for index in range(m):
        print(line[m-1 - index],end="")
    print()