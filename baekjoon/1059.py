from sys import stdin 
"""
    전략 
    n을 포함 하는 구간이고, 집합의 원소가 구간안에 없으면 
        -> 좋은 구간
    구간의 시작이 n보다 크면 종료, 구간의 끝이 n보다 작으면 스킵, 
    구간에 집합의 원소가 하나라도 있는지 확인
        -> 삼중 포문으로 구현 가능
"""

l = int(stdin.readline().strip())
set_of_ints = list(map(int,stdin.readline().strip().split()))
n = int(stdin.readline().strip())
count = 0
for start in range(1,1000 + 1):
    if start > n:
        break
    is_good = True 
    for end in range(start+1,1000 + 1):
        if end < n:
            continue
        for int_num in set_of_ints:
            if start <= int_num <= end:
                is_good = False
                break
        if is_good:
            count += 1
print(count)