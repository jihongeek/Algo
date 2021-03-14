def npr(n,r):
    k = 1
    for i in range(n,n-r,-1):
        k = k * i
    return k
def ncr(n,r):
    return int(npr(n,r)/npr(r,r))

sum_ncr = 0
k = -1
inputstr_mapped = list(map(int,input().split()))

r = inputstr_mapped[0] - 1
c = inputstr_mapped[1] - 1  
w = inputstr_mapped[2]


for i in range(r,r+w):
    k = k + 1
    for j in range(c,c+k+1):
        sum_ncr = sum_ncr + ncr(i,j)
    
print(sum_ncr)