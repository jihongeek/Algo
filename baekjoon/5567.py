# 파이썬의 빠른 출력
from sys import stdin
# 파이썬의 큐 
from collections import deque

def bfs(person):
    # 전역변수 설정
    global visited,n,mates
    # 큐 만들기 
    q = deque()
    # 친구관계를 확인한 사람 표시
    visited[person-1] = True
    q.append((person,0))
    # 초대된 친구 수를 저장할 변수
    invitedMates = 0
    while (len(q) > 0):
        # nowPerson의 값은 튜플! (사람번호,친구관계) 친구관계는 1이면 친구, 2이면 친구의 친구
        nowPerson = q.pop() # 큐에서 꺼내서 저장!! 
        # 친구관계가 2보다 크거나 같으면 넘기기 (어짜피 친구의 친구까지는 이미 초대확인) 
        if nowPerson[1] >= 2:
            continue
        # i는 사람번호! 역시 0보다 큰 수가 사람번호이기에 1개씩 밀려서 마지막 i가 n이 됨
        for i in range(1,n+1):
            # 친구관계를 이미 확인한 사람인지, 아니면 친구관계가 있는지 확인하기
            if not visited[i-1] and mates[nowPerson[0]-1][i-1]:
                # 친구관계 확인 표시!
                visited[i-1] = True
                # 아까 큐에서 뽑은 사람의 "친구관계 + 1"해서 큐에 푸시 
                q.append((i,nowPerson[1]+1))
                # 초대된 친구에 1추가하기
                invitedMates += 1
    # 초대된 친구 수 출력
    return invitedMates

# 사람 수 입력
n = int(stdin.readline().strip())
# 친구 관계 수 입력
m = int(stdin.readline().strip())

# 친구 관계(그래프)를 2차원 리스트(인접 행렬)로 나타내기!
mates = [[False]*n for _ in range(n)]

# 친구 관계를 확인을 표시할 리스트를 만들기   
visited = [False]*n 

for i in range(m):
    person1, person2 = map(int, stdin.readline().split())
    # 사람의 번호는 1번 부터! 인덱스에 1 빼줍니다.
    mates[person1-1][person2-1] = True
    mates[person2-1][person1-1] = True
print(bfs(1))