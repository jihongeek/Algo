from sys import stdin

"""
    key 함수를 이용 : 다항 함수를 이용한 정렬
"""
player_records = []
n = int(stdin.readline().strip())

for i in range(n):
    player_data = list(map(int,stdin.readline().strip().split()))
    player_num = player_data[0]
    multiplied_score = player_data[1] * player_data[2] * player_data[3]
    summed_score = player_data[1] + player_data[2] + player_data[3]
    player_record = (player_num,(40*multiplied_score)**3+(40*summed_score)**2+player_num)
    player_records.append(player_record)
player_records = sorted(player_records, key=lambda record : record[1])[:3]
for player_record in player_records:
    print(player_record[0], end= " ")