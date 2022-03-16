from sys import stdin 

"""
    누적합을 이용해서 i~j 수의 합이 m인 경우의 수 찾기
    -> 누적배열[j] - 누적배열[i-1] == m
"""

# 1 ~ n까지 누적합을 저장하는 리스트
cummulated_sums = [0]

# n : 주어지는 수열의 길이, m : i~j 수의 합과 비교할 수
n,m = map(int,stdin.readline().strip().split())
# 입력 받은 수열을 list 형태로 저장
sequence = [0] + list(map(int,stdin.readline().strip().split()))

# 누적합 저장
for index in range(1,n+1):
    cummulated_sums.append(cummulated_sums[index-1] + sequence[index])

# i~j 수의 합이 m인 경우의 수 세기
case_count = 0 
for i in range(1,n+1):
    for j in range(i,n+1):
        if cummulated_sums[j] - cummulated_sums[i-1] == m:
            case_count += 1 
print(case_count)

