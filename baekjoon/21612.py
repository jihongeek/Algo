from sys import stdin

"""
    주어진 입력 값을 이용해 기압을 계산하고 위치를 출력하기 
"""
boiling_point = int(stdin.readline().strip())
atmospheric_pressure = 5*boiling_point - 400
print(atmospheric_pressure)
if atmospheric_pressure == 100: # 해수면 위치 (sea level)
    print(0)
elif atmospheric_pressure < 100: # 해수면 보다 위 (above sea level)
    print(1) 
elif atmospheric_pressure > 100: # 해수면 보다 아래(below sea level)
    print(-1)
