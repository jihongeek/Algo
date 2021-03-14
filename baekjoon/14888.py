from sys import stdin

# 계산함수 
def calculate(nowIndex,nowValue,operatorNums):
    # 전역변수 지정하기 
    global n,maxValue,minValue
    # 현재 인덱스가 마지막이면
    if nowIndex == n-1:
        # 현재 계산값과 최대,최소 비교해서 최대,최솟값 갱신하기 
        maxValue = max(maxValue,nowValue) 
        minValue = min(minValue,nowValue)
        # 리턴        
        return
    else:
        """
         재귀호출시 매개 변수는 
         nowIndex: 다음 숫자의 인덱스, 
         nowValue: 다음 숫자를 계산한 값, 
         operatorNums: 해당 연산자의 갯수를 뺀 리스트 
        """
        # 덧셈 연산자가 있으면
        if operatorNums[0] > 0:
            calculate(nowIndex+1, nowValue+nums[nowIndex+1], [operatorNums[0]-1,operatorNums[1],operatorNums[2],operatorNums[3]])
        # 뺄셈 연산자가 있으면
        if operatorNums[1] > 0:
            calculate(nowIndex+1, nowValue-nums[nowIndex+1], [operatorNums[0],operatorNums[1]-1,operatorNums[2], operatorNums[3]])
        # 곱셈 연산자가 있으면
        if operatorNums[2] > 0:
            calculate(nowIndex+1, nowValue*nums[nowIndex+1], [operatorNums[0],operatorNums[1],operatorNums[2]-1,operatorNums[3]])
        # 나눗셈 연산자가 있으면
        if operatorNums[3] > 0:
            # 음수의 나눗셈이면
            if nowValue < 0:
                # 양수로 바꾸고 몫만 계산 후 음수로 변환 
                calculate(nowIndex+1, -1*(abs(nowValue)//nums[nowIndex+1]), [operatorNums[0],operatorNums[1],operatorNums[2],operatorNums[3]-1])
            else:
                # 몫만 계산
                calculate(nowIndex+1, nowValue//nums[nowIndex+1], [operatorNums[0],operatorNums[1],operatorNums[2],operatorNums[3]-1])
        return
# 나올 수 있는 최솟값을 최대로 잡기
maxValue = -1000000000
# 나올 수 있는 최댓값을 최소로 잡기 
minValue = 1000000000
# 숫자의 갯수 입력 받기 
n = int(stdin.readline().strip())
# 숫자들 입력 받기 
nums = list(map(int, stdin.readline().strip().split()))
# 연산자의 갯수 입력 받기
operatorNums =list(map(int, stdin.readline().strip().split()))
# 계산 시작!
calculate(0,nums[0],operatorNums)

# 최대 최소 
print(maxValue)
print(minValue)