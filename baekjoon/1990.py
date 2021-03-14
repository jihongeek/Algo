def thesieve():
    for i in range(0,n+1):
        numbers[i] = i
    for i in range(2,n+1):
        if numbers[i] == 0:
            continue
        for j in range(2*i,n+1,j+i):
            if numbers[j] == 0:
                continue
            else:
                numbers[j] = 0

num  = list(map(int,input().split()))

m = num[0]
n = num[1]
numbers = [i for i in range(100000000)]

thesieve()
    
for i in range(m,n+1):
    if numbers[i]!=0:
        print(numbers[i])

