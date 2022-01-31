from sys import stdin 
"""
    전략
        바구니를 공 개수 크기의 배열로 만들고 각 인덱스에 
        i+1 숫자(공)를 저장한다.
        입력 받은 두 바구니의 번호 - 1 인덱스로 서로의 공을 swap한다.
"""
n,m = map(int, stdin.readline().strip().split())
basket = [str(ball) for ball in range(1,n+1)]
for _ in range(m):
    i,j = map(int,stdin.readline().strip().split())
    basket[i-1],basket[j-1] = basket[j-1],basket[i-1]
print(" ".join(basket))