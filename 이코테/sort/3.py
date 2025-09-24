from sys import stdin

"""
전략: 
학생의 성적이 100 이하의 자연수(1~100) 이므로 계수 정렬을 사용하면 시간복잡도 (O(n+k)의 시간복잡도로 풀 수 있다)

성적을 인덱스로 하고, 해당 성적을 같는 학생 이름의 배열을 요소로 생각하는 2차원 리스트로 구현할 수 있다. 
그리고 출력을 할 때 1점부터 100점까지의 사람을 각 점수마다 출력하면 된다.
"""

n = int(stdin.readline().strip())
score_name_array = [ [] for _ in range(101)]

for _ in range(n):
  name, score_string = stdin.readline().strip().split(" ")
  score_name_array[int(score_string)].append(name)

for score in range(1,101):
  if len(score_name_array[score]) > 0:
    print(" ".join(score_name_array[score]), end= " ") 
