from sys import stdin

"""
    0 1 2 3
    N E S W
    +1 우향우
    +2 뒤로돌아
    -1 좌향좌
    4+(지시) % 4
"""

direction_alphabet = ["N","E","S","W"]
direction = 0
commands = [1,2,-1]
for i in range(10):
    t = int(stdin.readline().strip())
    direction = (direction + commands[t-1]) % 4
print(direction_alphabet[direction])