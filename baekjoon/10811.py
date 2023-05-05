from sys import stdin

n,m = map(int,stdin.readline().strip().split())
baskets = [ basket_number for basket_number in range(n+1)]
for _ in range(m):
    i,j = map(int,stdin.readline().strip().split())
    index_to_change = j 
    for basket_number in range(i,(i+j)//2+1):
        baskets[basket_number], baskets[index_to_change] = baskets[index_to_change], baskets[basket_number]
        index_to_change -= 1
for basket_number in range(1,n+1):
    print(baskets[basket_number], end = " ")
print("")
