from sys import stdin
now_order = 0
def visit(row,col,n,order):
    global visited,now_order
    if n == 0:
        if row == r and col == c:
            print(order)
        now_order += 1
        return
    move_size = 2**(n-1)
    if row <= r < row + move_size and col <= c < col + move_size:
        visit(row,col,n-1,order+move_size**2*0)
    if row <= r < row + move_size and col+move_size <= c < 2**origin_n:
        visit(row,col+move_size,n-1,order+move_size**2*1)
    if row+ move_size<= r < 2**origin_n and col <= c < col + move_size:
        visit(row+move_size,col,n-1,order+move_size**2*2)
    if row+ move_size<= r < 2**origin_n and col+move_size <= c < 2**origin_n:
        visit(row+move_size,col+move_size,n-1,order+move_size**2*3)
origin_n,r,c = map(int,stdin.readline().strip().split())
visit(0,0,origin_n,0)
