from sys import stdin 

def deleteNode(index):
    for child in range(n):
        if tree[index][child] == 1:
            deleteNode(child)
    tree[index] = [-1]*n
        
count = 0
n = int(stdin.readline().strip())
tree = [[0]*n for _ in range(n)]

for child,parent in enumerate(stdin.readline().strip().split()):
    if parent == "-1":
        continue
    parent = int(parent)
    tree[parent][child] = 1

toDelete = int(stdin.readline().strip())
deleteNode(toDelete)

for parent in range(n):
    for child in range(n):
        if tree[parent][toDelete] == 1:
            tree[parent][toDelete] = 0
    if tree[parent] == [0]*n:
        count += 1
print(count)   