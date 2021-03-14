import sys

def npr(n,r):
    k = 1
    for i in range(n,n-r,-1):
        k = k * i
    return k
def ncr(n,r):
    return int(npr(n,r)/npr(r,r))

t = int(input())

for i in range(t):
    inputnums = sys.stdin.readline().strip().split()
    print(ncr(int(inputnums[1]),int(inputnums[0])))
