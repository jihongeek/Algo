from sys import stdin

woods = list(map(int, stdin.readline().strip().split()))

for i in range(len(woods)):
    for j in range(len(woods)-1):
        if woods[j] > woods[j+1]:
            woods[j],woods[j+1] = woods[j+1],woods[j]
            print(" ".join(map(str,woods)))