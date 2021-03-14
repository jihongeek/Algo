from sys import stdin 

n,m = map(int,stdin.readline().strip().split())
unheards = sorted([stdin.readline().strip() for _ in range(n)]) 
unseens = set([stdin.readline().strip() for _ in range(m)]) 
unheardAndUnseens = [] 
count = 0
for unheard in unheards:
    if unheard in unseens:
        unheardAndUnseens.append(unheard)
print(len(unheardAndUnseens))
for i in unheardAndUnseens:
    print(i)