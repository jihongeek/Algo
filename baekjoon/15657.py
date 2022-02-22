from sys import stdin

def select(selected):
    if len(selected) == m:
        print(*selected)
        return
    for index in range(n):
        if len(selected) == 0 or selected[-1] <= numbers[index]:
            select(selected + [numbers[index]])
n,m = map(int,stdin.readline().strip().split())
numbers = list(map(int,stdin.readline().strip().split()))
numbers.sort()
select([])