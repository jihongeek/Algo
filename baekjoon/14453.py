from sys import stdin

"""

Hoof, Paper, Scissors 그냥 Rock, Paper, Scissors

Bessie는 Farmer John이 내는 동작을 예상할 수 있지만,
게을러서 동작을 한번 밖에 바꾸지 못한다. 
이 때 Bessie가 최대로 이길 수 있는 수를  구하는 것이 문제이다.

경우의 수
하나의 동작만 계속 내는 경우 Hoof, Paper, Scissors 3가지 경우

1,2~N 1번째는 내고 2번째 부터 다른 거 내거나 그냥 내기 
1~2,3~N 1~2번 째는 내고 3번째 부터 다른 거 내거나 그냥 내기
...
1~ i, i+1 ~ N 1~i번째 까지는 내고 i+1 번째 부터 다른거 내거나 그냥 내기

구간으로 접근 
말굽 가위 보를 배열로 생각하고 bessie가 이기는 경우를 하나의 배열로 또 생각

만약 Farmer John이 낸 동작이 PPHPS라면 bessie가 모두 이기는 동작은 SSPSH
이 SSPSH랑 bessie가 가능한 말굽 가위 보 배열을 만들어서 최대한 비슷하면 bessie가 많이 이길 수있는 
최고의 경우이고 같은 동작의 갯수를 출력하는 것이 정답이다.
-> 하지만 이 경우에는 최대 100000길의 배열을 300000가지의 배열과 비교해야 하기 때문에 시간복잡도 상으로 문제가 있다.

그 대신, 누적합을 이용해서 위에서 이야기한 구간별 가장 많이 나온 동작의 수를 더해서 구하는 방법을 생각했다. 

"""
n = int(stdin.readline().strip())
fj_gestures = []
for i in range(n):
    fj_gestures.append(stdin.readline().strip())

sum_of_gestures = [ [0]*(n+1) for _ in range(3) ]

# 누적합으로 동작의 수 저장
for i,gesture in enumerate(fj_gestures):
    if gesture == "H":
        sum_of_gestures[0][i+1] = sum_of_gestures[0][i] + 1
        sum_of_gestures[1][i+1] = sum_of_gestures[1][i]
        sum_of_gestures[2][i+1] = sum_of_gestures[2][i]
    elif gesture == "P":
        sum_of_gestures[0][i+1] = sum_of_gestures[0][i]
        sum_of_gestures[1][i+1] = sum_of_gestures[1][i] + 1
        sum_of_gestures[2][i+1] = sum_of_gestures[2][i]
    elif gesture == "S":
        sum_of_gestures[0][i+1] = sum_of_gestures[0][i]
        sum_of_gestures[1][i+1] = sum_of_gestures[1][i]
        sum_of_gestures[2][i+1] = sum_of_gestures[2][i] + 1

max_win = 0
for i in range(1,n+1):
    # 구간의 앞 부분에서 가장 많이 나온 동작의 수 구하기
    max_win_on_first = sum_of_gestures[0][i] - sum_of_gestures[0][1-1]
    max_win_on_first = max(max_win_on_first, sum_of_gestures[1][i] - sum_of_gestures[1][1-1])
    max_win_on_first = max(max_win_on_first, sum_of_gestures[2][i] - sum_of_gestures[2][1-1])
    # 구간의 뒷 부분에서 가장 많이 나온 동작의 수 구하기 
    max_win_on_second = sum_of_gestures[0][n] - sum_of_gestures[0][i+1-1]
    max_win_on_second = max(max_win_on_second, sum_of_gestures[1][n] - sum_of_gestures[1][i+1-1])
    max_win_on_second = max(max_win_on_second, sum_of_gestures[2][n] - sum_of_gestures[2][i+1-1])
    # 앞,뒤 구간에서 가장 많이 나온 동작의 수, 즉 Bessie가 가장 많이 이길 수 있는 수 
    max_win = max(max_win,max_win_on_first+max_win_on_second)

print(max_win)
