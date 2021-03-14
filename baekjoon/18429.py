n,k = map(int, input().split())
kits = list(map(int,input().split()))
# 가능한 경우의 수를 저장할 변수 
count = 0
# now : 남은 일수, weight : 중량, kitUsed : 사용된 운동키트들의 번호 
def findCase(now,weight,kitUsed):
    # count 전역변수 설정
    global count
    # 중량이 500보다 작아지면 성립하지 않으므로 종료
    if weight < 500:
        return
    # 기본단계 : now가 0
    if now == 0:
            count = count + 1
            return
    else:
        for i in range(n): # 0 ~ n-1 , i++
            # 사용할 운동키트가 사용되었는지 확인
            if i+1 not in kitUsed:
                # 사용되지 않았다면, 재귀호출
                findCase(now - 1,weight-k+kits[i],kitUsed+[i+1])

findCase(n,500,[])
print(count)