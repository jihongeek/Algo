from sys import stdin 

n,m = map(int,stdin.readline().strip().split())

def permuFunc(start, n, c):
    if c == 0:
        print()
        return
    print(start,end=" ")
    for i in range(start+1,n+1):
        permuFunc(i,n,c-1)

permuFunc(1,n,m)
    
