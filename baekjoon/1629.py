from sys import stdin

def lognPow(a,e,c):
    if e == 0:
        return 1
    elif e == 1:
        return (a*e)%c
    elif e % 2 == 0:
        n = lognPow(a,e//2,c)
        return (n*n)%c
    else:
        n = lognPow(a,(e-1),c) 
        return (n*a)%c

a,b,c = map(int, stdin.readline().split())
print(lognPow(a,b,c))