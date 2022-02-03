from sys import stdin
"""
    전략 : 
        입력 받은 수열을 오름차순으로 정렬 후,
        재귀함수로 수열 출력, 수열의 중복이 없게 하기 위해 집합 자료형 사용
        종료 조건 : count == m
        호출 조건 : 
            index == -1 -> 함수가 처음 호출 되었을 때
            numbers[index] <= numbers[new_index]
"""

def print_series(index,count,series):
    if count == m:
        series_str = " ".join(list(map(str,series)))
        # 현재의 수열이 이미 출력되었으면 출력하지 않고 넘기기
        if series_str in printed:
            return
        # 출력한 수열을 담는 집합 자료형에 현재 수열 저장 
        printed.add(series_str)
        print(series_str)
        return
    for new_index in range(n):
        # 비내림차순으로 정렬되어야 한다.
        # 또한 단축 회로 원리에 의해 index가 -1일 경우를 먼저 검사해야 한다. 
        if index == -1 or numbers[index] <= numbers[new_index]:
            print_series(new_index,count+1,series+[numbers[new_index]])
printed = set()
n,m = map(int, stdin.readline().strip().split())
numbers = list(map(int,stdin.readline().strip().split()))
numbers.sort()
print_series(-1,0,[])