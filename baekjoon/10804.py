from sys import stdin 
"""
    전략:
        구간 [a,b]를 받아서 b-a+1/2까지 대칭을 이용해
        카드를 역으로 배치한다. 
        cards[i] = cards[a+b-i],cards[a+b+i] = cards[i]
"""
cards = [str(x) for x in range(0,21)]

for _ in range(10):
    a,b = map(int,stdin.readline().strip().split())
    for i in range(a,(a+b)//2+1):
        cards[i],cards[a+b-i] = cards[a+b-i],cards[i]
print(" ".join(cards[1:]))
