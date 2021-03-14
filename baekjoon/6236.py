from sys import stdin

cost = 0
remain = 0
n,m = map(int,input().split())
bank = [int(stdin.readline().strip()) for x in range(n)]

left = 1
right = sum(bank)

while left < right:
    mid = (left + right) // 2
    
