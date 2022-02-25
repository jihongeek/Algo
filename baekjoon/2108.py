from sys import stdin
"""
    전략:
    한 루프에서 산술평균,수 갯수,범위 구하기
    최빈값을 구할 때, 수가 오름 차순이게 정렬 후, 
    가장 앞의 숫자가 같을 경우 다음 수를 출력
"""

number_frequencies = dict()
numbers = []
single_numbers = []
sum_of_numbers = 0
min_of_numbers = 4001
max_of_numbers = -4001

n = int(stdin.readline().strip())
for _ in range(n):
    number = int(stdin.readline().strip())
    sum_of_numbers += number

    max_of_numbers = max(number, max_of_numbers)
    min_of_numbers = min(number, min_of_numbers)
    
    numbers.append(number)

    if number not in number_frequencies:
        number_frequencies[number] = 1
        single_numbers.append(number)
    else:
        number_frequencies[number] += 1
print(round(sum_of_numbers/n))
numbers.sort()
print(numbers[n//2])
single_numbers.sort(key = lambda x : (-number_frequencies[x],x))

if len(single_numbers) == 1:
    print(numbers[0])
elif number_frequencies[single_numbers[0]] == number_frequencies[single_numbers[1]]:
    print(single_numbers[1])
else:
    print(single_numbers[0])
print(max_of_numbers-min_of_numbers) 