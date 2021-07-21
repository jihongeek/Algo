from sys import stdin 

n,k = map(int,stdin.readline().strip().split())
numbers = [x for x in range(2,n+1)]
index = 0
for i in range(0,n-1):
    if numbers[i] != False:
        for j in range(i,n-1,numbers[i]):
            if numbers[j] != False:
                index += 1
                ans = numbers[j] 
                numbers[j] = False
                if index == k:
                    break
        if index == k:
            break
print(ans)

