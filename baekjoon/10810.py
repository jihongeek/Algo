from sys import stdin

n,m = map(int,stdin.readline().strip().split())
baskets = [0]*(n+1)
for _ in range(m):
    i,j,k = map(int,stdin.readline().strip().split())
    for now_basket in range(i,j+1):
        baskets[now_basket] = k
for now_basket in range(1,n+1):
    print(baskets[now_basket], end = " ")
