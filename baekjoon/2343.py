from sys import stdin

n,m = map(int,stdin.readline().strip().split())
lessons = list( map(int, stdin.readline().strip().split()) )

# 가능한 블루레이의 길이 중에서 가장 작은 값을 촬영한 레슨중에서 가장 길이가 긴 값으로 한다.
left = max(lessons) 
  
# 가능한 블루레이의 길이 중에서 가장 큰 값을 촬영한 레슨들의 합으로 한다.
right = sum(lessons)

while left <= right:
    mid = (right+left)//2
    # 블루레이 디스크의 개수 
    bluray = 0
    # 현재 블루레이의 길이 
    bluraysize = 0

    for length in lessons:
        # 현재 블루레이에 들어가 있는 영상의 총 길이 + 추가할 레슨 의 길이가 현재 블루레이 길이보다 길때 
        if bluraysize + length > mid:
            bluray += 1
            bluraysize = 0
        bluraysize += length

    if bluraysize > 0:
        bluray += 1
    else:
        bluray += 0
    # 현재 블루레이 디스크의 개수가 원하는 개수보다 작으면 디스크당 레슨의 총 길이가 작아져야함!
    if bluray <= m:
        right = mid - 1
    # 아니면 커져야 함!
    else:
        left = mid + 1
print(left)


    
     
