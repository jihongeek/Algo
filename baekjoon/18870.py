from sys import stdin

n = int(stdin.readline().strip())
locations = list(map(int,stdin.readline().strip().split()))
locationsSorted = sorted(list(set(locations)))


for toFind in locations:
    left = 0
    right = len(locationsSorted) - 1
    while left <= right:
        mid = (left+right)//2
        if toFind > locationsSorted[mid]:
            left = mid + 1
        elif toFind < locationsSorted[mid]:
            right = mid - 1
        else:
            print(mid, end = " ")
            break





