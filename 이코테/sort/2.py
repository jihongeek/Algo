from sys import stdin 
"""
  입력을 내림차순으로 정렬된 결과로 출력하기
"""
n = int(stdin.readline().strip())
sequence = [int(stdin.readline().strip()) for _ in range(n)]
sequence.sort(reverse=True)

for number in sequence:
  print(number, end=" ")