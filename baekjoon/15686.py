from sys import stdin

"""
    전략 : 치킨집을 기준으로 치킨집 ~ 집까지의 거리를 계속 최소값으로
    최신화 하고 합들을 구해서 최소 도시의 치킨거리 구하기 
"""
def calc_distance(house_row,house_col,chicken_row,chicken_col):
    distance = abs(house_row-chicken_row)
    distance += abs(house_col-chicken_col)
    return distance
def calc_city_distance():
    city_distance = 0
    for house_row,house_col in house_locations:
        distance = distance_board[house_row][house_col]
        if distance != MAX_DISTANCE:
            city_distance += distance
    return city_distance

def choose_chicken(now_chicken_index,count):  
    global min_city_distance 
    if count == m:
        return     
    changed_cases = []
    now_chicken_row,now_chicken_col = chicken_locations[now_chicken_index]
    # 각 집집마다 치킨거리 구해서 최소값으로 최신화
    for house_row,house_col in house_locations:
        last_distance = distance_board[house_row][house_col]
        distance = calc_distance(house_row,house_col,now_chicken_row,now_chicken_col)
        if distance < last_distance:
            changed_cases.append((house_row,house_col,last_distance)) # (row,col,last_value)
            distance_board[house_row][house_col] = distance             
    calculated_city_distance = calc_city_distance()
    min_city_distance = min(min_city_distance,calculated_city_distance)               
    # 다음 치킨집 선택
    for next_chicken_index in range(now_chicken_index+1,len(chicken_locations)): 
        choose_chicken(next_chicken_index,count+1)
    # 최신화 해주었던 집에 대한 치킨거리 원상 복구
    for changed_row,changed_col,last_distance in changed_cases:
        distance_board[changed_row][changed_col] = last_distance
            
n,m = map(int,stdin.readline().strip().split())
MAX_DISTANCE = 50**2
chicken_locations = []
house_locations = []
min_city_distance = MAX_DISTANCE*n*n
for row in range(n):
    for col,space in enumerate(stdin.readline().split()):
        if space == "1":
            house_locations.append((row+1,col+1))
        elif space == "2":
            chicken_locations.append((row+1,col+1))
for index in range(len(chicken_locations)):
    distance_board = [[MAX_DISTANCE]*(n+1) for _ in range(n+1)]
    choose_chicken(index,0)
print(min_city_distance)