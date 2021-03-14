from sys import stdin

# 움직일려는 곳이 체스판 위에 있는지 확인하는 함수 
def isInBoard(location):
    # location[0] 은 행, location[1]은 열 
    if  0 < location[0] < 9 and 0 < location[1] < 9: # 1~8
        return True
    else: 
        return False 
# 킹의 마지막 위치, 돌의 마지막 위치, 킹의 이동 수 받아서 저장         
kingLast,stoneLast,n = stdin.readline().strip().split()

# 킹,돌의 마지막 위치를 [행, 열]로 변환 (단, 체스판의 행과 열은 1부터 시작)  
kingLast = [int(kingLast[1]), ord(kingLast[0])-ord('A')+1]
stoneLast = [int(stoneLast[1]), ord(stoneLast[0])-ord('A')+1]

# 문자 n을 숫자로 변환 
n = int(n)
# 킹의 움직임을 n번 만큼 입력 받아 저장 
moves = [stdin.readline().strip() for _ in range(n)]

# 가능한 킹의 이동을 딕셔너리(해시 테이블)로 저장 [행의 이동,열의 이동]
kingMove = {
    'R' : [0,1],
    'L' : [0,-1],
    'B' : [-1,0],
    'T' : [1,0],
    'RT' : [1,1],
    'LT' : [1,-1],
    'RB' : [-1,1],
    'LB' : [-1,-1]
}

# 킹의 움직임을 하나식 꺼내서 이동시키는 for 루프 
for move in moves:
    # 이동할려는 위치가 돌의 위치와 겹치는지 확인 
    if [ kingLast[i] + kingMove[move][i] for i in range(2)] ==  stoneLast: # [a1,b1] + [a2,b2] = [a1+a2,b1+b2]
        # 겹치고, 돌의 이동할려는 위치가 체스판 안에 있을 때 
        if isInBoard([ stoneLast[i] + kingMove[move][i] for i in range(2)]):
            # 돌 옮기기 
            stoneLast = [ stoneLast[i] + kingMove[move][i] for i in range(2)]
        # 체스판 밖에 있으면 다음 움직임으로 넘어가기 
        else: 
            continue
    # 킹이 이동할려는 위치가 체스판 안에 있으면
    if isInBoard([ kingLast[i] + kingMove[move][i] for i in range(2)]) :
        # 킹 옮기기 
        kingLast = [ kingLast[i] + kingMove[move][i] for i in range(2)]
    # 없으면 마찬가지로 다음 움직임으로 넘어가기 
    else:
        continue

# 체스판의 형식으로 위치를 바꿔서 킹과 돌의 위치 출력하기  
print(chr(kingLast[1] + ord('A')-1) + str(kingLast[0]))
print(chr(stoneLast[1] + ord('A')-1) + str(stoneLast[0]))