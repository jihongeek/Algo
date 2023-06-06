from sys import setrecursionlimit
setrecursionlimit(10**5)
n = int(input())

"""
    어짜피 열이랑, 행, 두방향 대각선에 퀸을 이전에 두었는지 확인하면 되니깐
    4Xn 배열을 만들어서 방문 여부 확인하기
"""
count = 0
def is_placeable(last_row,last_col,row,col):
    if not (0 <= row <= n and 0 <= col <= n):
        return False
    if visited[0][row] is True or visited[1][col] is True:
        return False
    if abs(abs(last_row) - abs(row)) == abs(abs(last_col) - abs(col)):
        return False
    if visited[2][row+col] is True or visited[3][col-row+(n-1)] is True:
        return False
    return True


def count_case(now_location,count_of_queen):
    global count,visited 
    if n == count_of_queen:
        count += 1
        return 
        
    now_row,now_col = now_location
    for col in range(0,n): 
        if is_placeable(now_row,now_col,now_row+1,col) is True:
            changed = [False]*4   
            for i,j in enumerate([now_row+1,col,now_row+1+col,col-(now_row+1)+(n-1)]):
                if visited[i][j] is False:
                    changed[i] = True
                    visited[i][j] = True               
            count_case((now_row+1,col),count_of_queen+1)
            for i,j in enumerate([now_row+1,col,now_row+1+col,col-(now_row+1)+(n-1)]):
                if changed[i] is True:
                    visited[i][j] = False
    return

for col in range(n):
    visited = [[False]*n,[False]*n,[False]*(2*(n-1)+1),[False]*(2*(n-1)+1)]
    visited[0][0] = True
    visited[1][col] = True
    visited[2][col] = True
    visited[3][col+(n-1)] = True
    count_case((0,col),1)        
print(count)