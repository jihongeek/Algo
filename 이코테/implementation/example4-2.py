from sys import stdin

"""
문제 설명
00시 00분 00초 부터 n시 59분 59초 까지 3이 있는 경우의 수 세기

전략 : 
그냥 세기 10으로 나누었을 때 몫이 3이거나, 나머지가 3이면 포함하는 거 아닌가?
(책에서는 일반 문자열로 "3" in str(시 분 초)로 세었음)
"""
n = int(stdin.readline().strip())
count = 0
for hour in range(n+1):
  for minute in range(60):
    for second in range(60):
      if hour // 10 == 3 or hour % 10 == 3:
        count += 1
        continue
      if minute // 10 == 3 or minute % 10 == 3:
        count += 1
        continue
      if second // 10 == 3 or second % 10 == 3:
        count += 1
        continue
      
      
print(count)