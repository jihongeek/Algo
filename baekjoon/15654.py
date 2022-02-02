from sys import stdin 
"""
    전략 : 
        재귀함수로 수열 출력하기
            매개변수 -> 출력 할 숫자의 갯수(count),
            , 출력 할 숫자 리스트 
                count 초기값 -> 0 , 리스트 []
            종료 조건 -> 출력한 숫자가 m개
            호출 조건 -> 새로운 인덱스일 때
"""

def print_number(count, to_print_numbers):
    if count == m:
        print(" ".join(to_print_numbers))
        return
    for new_index in range(n):
        if str(numbers[new_index]) not in to_print_numbers:
            print_number(count+1,to_print_numbers+[str(numbers[new_index])])

n,m = map(int, stdin.readline().strip().split())
numbers = list(map(int,stdin.readline().strip().split()))
numbers.sort()
printed = [False]*n 

print_number(0, [])
