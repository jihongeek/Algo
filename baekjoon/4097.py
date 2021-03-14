import sys

while (1):
    n = int(input()) 
    if n == 0: # 0이 들어 오면 종료
        break
    benefits = [] # 이익 값을 담을 리스트
    for i in range(n):
        benefits.append(int(sys.stdin.readline().strip())) # 입력받은 값(문자) -> 정수 해주고 benefits 리스트에 넣어주기 

    maxes = [0]*len(benefits) # benefits의 원소 갯수 만큼 원소가 0인 리스트 만들기 (최댓값을 담는)
    maxes[0] = benefits[0] # 첫번째 원소를 마지막으로 하는 수열의 합의 최댓값 == 그냥 첫번째 원소

    for i in range(1,n):
        maxes[i] = max(0,maxes[i-1]) + benefits[i] 
    print(max(maxes))