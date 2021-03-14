import sys

num = int(input())

for i in range(num):
    s_list = sys.stdin.readline().strip().split()
    for i,j in enumerate(s_list):
        s_list[i] = "".join(reversed(j))
    print(" ".join(s_list))