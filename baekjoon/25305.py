from sys import stdin 
n,k = map(int,stdin.readline().strip().split())
scores = list(map(int,stdin.readline().strip().split()))
scores.sort(reverse=True)
print(scores[k-1])