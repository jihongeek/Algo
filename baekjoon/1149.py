from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
n = int(stdin.readline().strip())

def get_min_cost(house_index,last_color):
    """
    house_index 부터 n 까지의 최소 비용을 구하는 함수
    """ 
    new_cost = 1000 * 1000
    
    # 재귀의 마지막
    if house_index == n:
        return costs_by_house[house_index][last_color]
    # 메모이제이션이 되어있다면(이미 계산했다면) 더 이상 진행하지 말고 계산값 반환  
    if memo[house_index][last_color] != -1:
        return memo[house_index][last_color]
    # 이전과 페인트 색이 같지 않거나 가장 처음 경우면 계산시작 
    for color in (0,1,2):
        if last_color != color or house_index == 0:
            new_cost = min(get_min_cost(house_index+1,color), new_cost)
    memo[house_index][last_color] = costs_by_house[house_index][last_color] + new_cost      
    return memo[house_index][last_color]

costs_by_house = [[0,0,0]]

memo = [[-1]*3 for _ in range(n+1)]

for _ in range(n):
    red_cost,green_cost,blue_cost = map(int,stdin.readline().strip().split())
    costs_by_house.append([red_cost,green_cost,blue_cost])

print(get_min_cost(0,0))

    