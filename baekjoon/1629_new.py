from sys import stdin

def fast_pow(x,n):
    if n == 0:
        return 1 % c
    if n % 2 == 1:
        return (x * fast_pow((x*x)%c, (n-1)//2) ) % c
    else:
        return fast_pow( (x*x)%c, n//2 ) % c
    
a,b,c = map(int,stdin.readline().strip().split())
print(fast_pow(a,b) % c)