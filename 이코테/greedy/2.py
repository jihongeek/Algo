from sys import stdin
"""
전략 : 

일단 가장 수가 큰 인덱스를 정렬하고, 현재 k 까지 반복해서 더하기,
갯수가 다 되면 다음 크기의 수 한 번 더하고 카운트 초기화 한다음 반복 

그렇다면 가장 크기가 큰 1번 2번 수만 있으면 되는 거 아닌가?

현재 가능한 가장 큰 수 더하기는 결국 

가장 큰 첫번째 수를 계속 더하되, k 만큼 연속되면, 두 번째 수 한번 더하고 다시 첫 번째 수 더하기

반례는 없을까? k가 1이여도 어짜피 m번 더해지는 수들의 집합은 최대가 되어야 하니 이것이 최선이다.
"""

n,m,k = map(int,stdin.readline().strip().split())
number_array = list(map(int, stdin.readline().strip().split()))
number_array.sort(reverse=True)

continuos_count = 0
summation = 0

for _ in range(m):
  # 같은 숫자가 k번 반복 되었을 때, 다음 큰 숫자를 더하고, 연속 카운트 초기화
  if continuos_count == k:
    summation += number_array[1]
    continuos_count = 0
    continue
  # 그렇지 않으면 가장 큰 숫자를 더하기
  summation += number_array[0]
  continuos_count += 1

print(summation)
