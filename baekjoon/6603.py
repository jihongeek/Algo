from sys import stdin 
"""
    전략 : 재귀를 이용해서 로또 번호를 출력한다.
    이미 출력한 번호로 이루어져 있으면 출력하면 안된다.
    -> 집합 자료형에 출력된 로또 번호를 넣어놓았다가, 
    -> 6개의 숫자를 골랐을 때 나왔던 조합이 아닐 경우 출력
"""
def print_lotto(count,selected_numbers):
    if count == 6:
        # 이미 출력한 로또 번호 조합일 경우 리턴
        if frozenset(selected_numbers) in printed:
            return
        for number in selected_numbers:
            print(number,end = " ")
        print()
        # 출력한 로또 번호에 추가
        printed.add(frozenset(selected_numbers))
    for number in set_of_num:
        if number not in selected_numbers:
            print_lotto(count + 1, selected_numbers+[number])
while True:
    printed = set() # 출력된 로또 번호의 조합을 저장하는 집합
    input_str = stdin.readline().strip().split()
    if input_str[0] == "0":
        break
    k = int(input_str[0])
    set_of_num = list(map(int,input_str[1:]))
    print_lotto(0,[])
    print()