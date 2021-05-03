from sys import stdin

a,b,c,d,e,f = map(int, stdin.readline().strip().split())

def solve(a,b,c,d,e): 
    for x in range(-999,1000):
        for y in range(-999,1000):
            if a*x+b*y == c and d*x+e*y == f:
                return (x,y)

x,y = solve(a,b,c,d,e)
print(f"{x} {y}")