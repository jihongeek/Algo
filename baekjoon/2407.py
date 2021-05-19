from sys import stdin
n,m = map(int,stdin.readline().strip().split())
factorials = dict()
combination = 0
def factorial(n):
    if n in factorials:
        return factorials[n]
    if n == 0:
        factorials[0] = 1
        return factorials[0]
    return n * factorial(n-1)
print((factorial(n)//factorial(n-m))//factorial(m))