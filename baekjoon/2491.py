n = int(input())
series = list(map(int,input().split()))

# 내림차순의 길이  
descend = 1
# 오름차순의 길이 
increase = 1
# 오름차순의 최대 길이 
maxOfincrease = 1
# 내림차순의 최대 길이 
maxOfdescend = 1

for i in range(n-1): # 0 ~ n - 2, i++
    # 오름차순의 경우 increase 1 증가
    if series[i] <= series[i+1]:
        increase += 1
    
    # 아니면 increase 를 1로 초기화  
    else:
        increase = 1
    
    # 오름차순의 최대길이를 갱신 
    maxOfincrease = max(increase,maxOfincrease)

for i in range(n-1): # 0 ~ n - 2, i++
    # 내림차순의 경우 descend 1 증가
    if series[i] >= series[i+1]:
        descend += 1
    
    # 아니면 descend 를 1로 초기화  
    else:
        descend = 1
    
    # 내림차순의 최대 길이를 갱신 
    maxOfdescend = max(descend,maxOfdescend)

# 오름차순의 최대 길이와 내림차순의 길이 중 더 긴 것을 출력  
print(f"{max(maxOfincrease,maxOfdescend)}")