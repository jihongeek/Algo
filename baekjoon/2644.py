from collections import deque 

# 가족의 부모 자식 관계를 나타내고 서로의 촌수를 저장하는 이차원 배열 
family = [[0]*101 for _ in range(101)]

# 방문 여부를 표시하는 이차원 배열 
visited = [[False]*101 for _ in range(101)]

def bfs(person1,person2):
    # 전역변수 설정
    global n, personToFind
    # 큐 만들기 
    q = deque()
    
    # 방문했음 표시하기 
    visited[person1][person2] = True
    visited[person2][person1] = True
    # 큐에 집어넣기 
    q.append( (person1,person2) )
    
    # bfs의 핵심!
    while len(q) > 0:
        person1,person2 = q.popleft()
        # 2번째 사람이 구할려는 사람이면 bfs 종료 
        if person2 == personToFind[1]:
            return (person1,person2)
        for i in range(n+1):
            # person2와 관계가 있고 아직 방문하지 않았으면
            if not visited[person2][i] and family[person2][i] > 0:
                
                # 방문했음 표시
                visited[person2][i] = True
                visited[i][person2] = True
                
                # 촌수에 1추가 하기
                family[person2][i] = family[person1][person2] + 1
                
                # 큐에 관계 집어넣기
                q.append( (person2,i) )
    return (0,0)



n = int(input())
personToFind = list(map(int,input().split()))
relation = 0
m = int(input())

# 부모와 자식 관계 촌수를 1로 해서 저장 
for i in range(m):
    x,y = map(int, input().split())
    family[x][y] = 1
    family[y][x] = 1

# 촌수를 찾을 두 사람중에서 첫 번째 사람과 관계 있는 사람들로 bfs시작
for i in range(n+1):
    # 방문하지 않았고, 자기 자신과의 관계가 아니고, 관계가 있으면,
    if visited[personToFind[0]][i] != True and i != personToFind[0] and family[personToFind[0]][i] > 0:
        x,y = bfs(personToFind[0],i)
        relation = family[x][y]
if relation == 0:
    print(-1)
else:
    print(relation)
