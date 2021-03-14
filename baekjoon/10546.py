from sys import stdin

# 마라토너 이름과 해당되는 사람 수를 저장하는 딕셔너리 
marathonerDict = dict()
# 마라토너의 이름이 저장되는 집합 
marathonerSet = set([])

# 총 마라토너의 수 입력받기 
n = int(input())
 
for i in range(n): # 0 ~ n-1 , i++
    # 마라토너 이름 입력 받기
    name = stdin.readline().strip()
    # 집합에 이름넣기  
    marathonerSet.add(name)

    # 입력받은 마라토너의 이름으로 key가 딕셔너리에 있으면 value를 1증가
    if name in marathonerDict:
        marathonerDict[name] += 1
    # 없으면 value를 1로 설정
    else:
        marathonerDict[name] = 1

for i in range(n-1): # 1명이 완주를 못하므로 0 ~ n-2, i++
    # 완주자 이름 입력받기 
    finisher = stdin.readline().strip()

    # 완주자 이름을 key로 삼아 딕셔너리의 value를 1감소 
    marathonerDict[finisher] -= 1 

    # 완주자 key의 딕셔너리 value 값이 0이 되면 집합에서 마라토너 이름 제거
    if marathonerDict[finisher] == 0:
        marathonerSet.remove(finisher)

# 집합을 리스트로 바꿔줘서 완주하지 못한 마라토너를 출력 
print(list(marathonerSet)[0])