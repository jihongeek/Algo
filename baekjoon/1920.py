import sys
n = sys.stdin.readline().strip()

anums = sys.stdin.readline().strip().split()
    
m = sys.stdin.readline().strip()
mnums = sys.stdin.readline().strip().split()

anums = sorted(anums)

for i in mnums:
    find = 0
    left = 0
    right = len(anums)-1
    while left <= right:
        mid = int((left+right)/2)
        if i == anums[mid]:
            find = 1
            break 
        elif i > anums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(find)
        
        

    