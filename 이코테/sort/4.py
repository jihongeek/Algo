from sys import stdin

"""
A의 크기를 가장 크게 할려면
A의 가장 작은 요소 k개와 B의 가장 큰 요소 k개를 맞교환 하면 된다.

즉 A 오름차순 정렬, B 내림차순 정렬하여 a[:k] = b[:k] 하고 sum(a) 하면 될 것 같다.
-> 오류가 있음 b에 있는 원소가 a보다 작을 수 있음 작을 경우만 교환 진행
"""

n, k = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
b = list(map(int, stdin.readline().strip().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] >= b[i]:
    break
  a[i],b[i] = b[i],a[i]
print(sum(a))