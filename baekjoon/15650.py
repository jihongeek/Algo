from sys import stdin 

n,m = map(int,stdin.readline().strip().split())
found = set([])
def permuFunc(n, c, choosed : list):
    if c == 0:
        if frozenset(choosed) not in found: 
            for i in choosed:
                print(f"{i}", end=" ")
            found.add(frozenset(choosed))
            print()
        return
    for i in range(choosed[-1]+1,n+1):
        permuFunc(n,c-1,choosed + [i])

for i in range(1,n+1):
    permuFunc(n,m-1,[i])

    
