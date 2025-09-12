from sys import stdin 

"""
전략(그리디)

가로 세로로 놓인 카드 중에서 행을 선택하여 카드를 뽑는데 가장
그 행에서 작은 수의 카드를 뽑아야 한다.

이때 가장 큰 수의 카드를 뽑기

-> 각 행의 카드 중에서 최소값이 가장 큰 카드에 적힌 수를 출력
-> 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있다.
"""

n,m = map(int, stdin.readline().strip().split())
cards = [ map(int, stdin.readline().strip().split()) for _ in range(n)]
min_cards_map = map(min,cards)

print(max(min_cards_map))