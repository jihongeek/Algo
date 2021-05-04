from sys import stdin 
a,b,c,n = map(int,stdin.readline().strip().split())

def isPossible(a,b,c,n):
    for i in range(0,n+1,a):
        for j in range(0,n+1,b):
            for k in range(0,n+1,c):
                if i+j+k == n:
                    return 1
    return 0

print(isPossible(a,b,c,n))