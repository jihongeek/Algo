from sys import stdin

# 모든 부분수열의 합 구하는 함수

def check_all_sums(now_index, now_sum, selected_term_indexes): 
    # 수열의 다음 항 선택하여 재귀호출로 합 찾아나가기
    for next_term_index in range(now_index+1,len(series)): # 같은 값의 다른 항이 존재할 수 있으므로 인덱스 사용
        if next_term_index not in selected_term_indexes:
            check_all_sums(next_term_index, now_sum+series[next_term_index], selected_term_indexes | set([next_term_index]))
    # 구한 현재 부분수열 합 집합에 저장
    set_of_sum.add(now_sum)

# 부분수열의 합이 아닌 것 중에 가장 작은 것을 구하는 함수
def check_not_sum():
    for i in range(1,2000001):
        if i not in set_of_sum:
            return i

# 항의 갯수 받기
n = int(stdin.readline().strip())

# 수열 저장하는 리스트
series = list(map(int,stdin.readline().strip().split()))

# 부분수열의 합을 저장하는 집합 자료형 (초기에는 수열의 항을 저장) 
set_of_sum = set()

# 모든 부분수열의 합 구하기
check_all_sums(-1,0,set())

# 1부터 검사하다가 없으면 그 수가 부분수열의 합으로 구할 수 없는 수 구해서 출력
print(check_not_sum())