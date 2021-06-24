from sys import stdin

arr = [[0]*30 for _ in range(30)]

n,k = map(int, stdin.readline().strip().split() )
for row in range(n):
    for col in range(row+1):
        if col == 0 or col == row:
            arr[row][col] = 1
        else:
            arr[row][col]  = arr[row-1][col] + arr [row-1][col-1]       
print(arr[n-1][k-1])