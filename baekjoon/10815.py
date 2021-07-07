from sys import stdin 

n = int(stdin.readline().strip())
cards = list(map(int,stdin.readline().strip().split()))
cards.sort()
m = int(stdin.readline().strip())

for i in list(map(int,stdin.readline().strip().split())):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left+right)//2 
        if i < cards[mid]:
            right = mid - 1
        elif i > cards[mid]:
            left = mid + 1
        else:
            break
    if cards[mid] == i:
        print(1,end=" ")
    else:
        print(0,end=" ") 