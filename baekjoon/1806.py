from sys import stdin

"""
    투포인터를 이용해 합이 S이상인 연속된 부분수열의 길이 구하기
"""

n,s = map(int,stdin.readline().strip().split())
sequence = list(map(int,stdin.readline().strip().split())) + [0]
sub_sum = 0
end = 0
start = 0
min_length = 100000
while end <= n:
    if sub_sum >= s:
        min_length = min(min_length,end - start)
        sub_sum -= sequence[start]
        start += 1
    else:
        sub_sum += sequence[end]
        end += 1
# 만약 초기 값과 길이가 같으면 합을 만드는 것이 불가하므로 0으로 값 변경
if min_length == 100000:
    min_length = 0 
print(min_length)
