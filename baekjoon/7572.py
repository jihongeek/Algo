from sys import stdin

"""
    전략
        시작은 4년째 부터 갑자년이고, 
        십간은 10년마다, 십이지는 12년마다 순환함을 이용 
"""
gan = [str(9)] + [str(x) for x in range(9)]
ji = ['L'] + [chr(ord('A') + x) for x in range(12)]
year = int(stdin.readline().strip())
print(ji[(year-3)%12]+gan[(year-3)%10])