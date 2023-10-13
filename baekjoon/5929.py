from sys import stdin

"""
문제 : 잘못 변환된(자릿수 하나가 잘못적힌) 이진수와, 삼진수로 원래의 십진수 숫자를 찾기

처음 생각했던 방법 : 이렇게 안하고 입력 받은 두수를 십진수로 바꾼다음에 작은 수 부터 큰 수까지 
이진수 삼진수로 바꾼다음 만약에 자릿수가 다른 게 각각 1자리 밖에 없다면 그 수가 정답이다.
-> 정답은 출력하나 시간초과;;

두번째 생각한 방법 : 일단 잘못 적을 수 있는 2진수 후보 숫자들을 다 계산해 두고 집합에 넣어둔 다음,
3진수 후보 숫자들을 계산해서 집합에 있는 지 확인하고 있으면 출력한다.
-> 통과

bessie가 잘못적은 경우의 수를 생각해보자
1010 => 4개
0010 1110 1000 1011
212 =>  6개 
012 202 210
112 222 211

즉 4*6 가지만 비교하면 된다. 
그리고 n의 최댓값은 1 billion, 
즉 10억이기 때문에 자릿수의 갯수도 얼마 없다. 
자릿수의 갯수는 2비트로 나타낼 수 있는 수의 경우의 수로 생각하면 알수있다.
"""

def base2_to_base10(base2 : str) -> int:
    base10 = 0
    for i, digit in enumerate(base2):
        base10 += ( 2**(len(base2)-1-i)*(ord(digit)-ord("0")) )
    return base10

def base3_to_base10(base3 : str) -> int:
    base10 = 0
    for i, digit in enumerate(base3):
        base10 += ( 3**(len(base3)-1-i)*(ord(digit)-ord("0")) )
    return base10
wrong_base2 = stdin.readline().strip()
wrong_base3 = stdin.readline().strip()

set_of_base2_cases = set()
# 2진수 후보 계산
for index,digit in enumerate(wrong_base2):
    if digit == "0":
        base2_case = base2_to_base10(wrong_base2[:index]+"1"+wrong_base2[index+1:])
    else:
        base2_case = base2_to_base10(wrong_base2[:index]+"0"+wrong_base2[index+1:])
    set_of_base2_cases.add(base2_case)

# 3진수 후보 계산
base3_cases = []
for index,digit in enumerate(wrong_base3):
    if digit == "0":
        base3_case_1 = base3_to_base10(wrong_base3[:index]+"1"+wrong_base3[index+1:])
        base3_case_2 = base3_to_base10(wrong_base3[:index]+"2"+wrong_base3[index+1:])
    elif digit == "1":
        base3_case_1 = base3_to_base10(wrong_base3[:index]+"0"+wrong_base3[index+1:])
        base3_case_2 = base3_to_base10(wrong_base3[:index]+"2"+wrong_base3[index+1:])
    elif digit == "2":
        base3_case_1 = base3_to_base10(wrong_base3[:index]+"0"+wrong_base3[index+1:])
        base3_case_2 = base3_to_base10(wrong_base3[:index]+"1"+wrong_base3[index+1:])
    base3_cases.append(base3_case_1)
    base3_cases.append(base3_case_2)

    
# 3진수 후보들 중에서 2진수 후보에도 있을 경우 정답!  
for base3_case in base3_cases:
    if base3_case in set_of_base2_cases:
        print(base3_case)  
    
