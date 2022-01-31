from sys import stdin 
"""
    규칙 : 분모 분자의 합을 이용?
    합이 홀 왼쪽 -> 분자 + 1 / 합 - 분자
        만약 합 - 1이 분자이면, 분자 + 1 / 분모  
    합이 짝 오른쪽 -> 합 - 분모/ 분모 + 1   
        만약 합 - 1이 분모이면,  분자 / 분모  + 1 
"""
numerator = 1
denominator = 1 
x = int(stdin.readline().strip())

for i in range(1,x):
    sum_of_frac = numerator+denominator
    if sum_of_frac % 2 == 0:
        if sum_of_frac - 1 == denominator:
            denominator += 1
        else:
            denominator += 1
            numerator = sum_of_frac - denominator
    else:
        if sum_of_frac - 1 == numerator:
            numerator += 1
        else:
            numerator += 1
            denominator = sum_of_frac - numerator
print(f"{numerator}/{denominator}")