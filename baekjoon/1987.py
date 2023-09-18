from sys import stdin,setrecursionlimit
# expand python recursion limit
setrecursionlimit(10**5)

"""
    strategy : visit alphabet that was not visited before with recursion!
"""

# check the location is visitable
def is_visitable(row,col):
    if not 0 <= row < r:
        return False 
    if not 0 <= col < c:
        return False 
    alphabet = board[row][col]
    # if alphabet of location is already visited
    if visited_alphabet[ord(alphabet)-ord("A")] is True:
        return False
    return True

def visit(row,col,count):
    max_count = count
    # check up,down,left,right location and visit
    for move in [(-1,0),(1,0),(0,-1),(0,1)]:
        row_move,col_move = move
        next_row,next_col = (row + row_move),(col+col_move)         
        if is_visitable(next_row,next_col) is True:
            next_alphabet = board[next_row][next_col]
            visited_alphabet[ord(next_alphabet)-ord("A")] = True
            max_count = max(visit(next_row,next_col,count+1),max_count) 
            # if single route visiting ends, unvisit last visit
            visited_alphabet[ord(next_alphabet)-ord("A")] = False
    return max_count

r,c = map(int,stdin.readline().strip().split())
visited_alphabet = [False]*26 # let visted_alphabet[index_of_alphabet] = visit 
board = []
for line in range(r):
    board.append(stdin.readline().strip())

# make a visit first location
first_alphabet_index = ord(board[0][0]) - ord("A")
visited_alphabet[first_alphabet_index] = True
print(visit(0,0,1))
