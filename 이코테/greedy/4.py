from sys import stdin

"""
전략 : n // k를 하면 남는 수가 1//k 이 되기 때문에 가능하면
2번 연산을 먼저 적용하고, 불가 하면 -1 하는 것이
최소 횟수로 나눌 수 있는 방법이다.

그리고 이 방법에 대한 검증을 하자면,
k로 나누는 것은 몇 번의 -1 연산하는 것으로 대체가 가능하기에
성립한다. -> 나눌 수 있다는 것

이렇게 시도하면 시간 복잡도는 O(n)

이게 정해 아닌가?
나누어 떨어지는 수가 될 수 있게 뺄셈을 한 번에 계산하는
방법이 있을 듯 
"""
count = 0
n,k = map(int, stdin.readline().strip().split())
while n > 1:
  if n % k == 0:
    n = n // k
    count += 1
    continue
  n -= 1
  count +=1

print(count)
