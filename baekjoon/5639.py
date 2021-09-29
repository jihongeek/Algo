from sys import stdin,setrecursionlimit
setrecursionlimit(20000)
def travel(key):
    if key == 0:
        return
    travel(bst[key]["leftChild"])
    travel(bst[key]["rightChild"])
    print(key)

rootNodeKey = 0
bst = {}
while True:
    inputNum = stdin.readline().strip()
    if inputNum == "":
        break
    nodeKey = int(inputNum) 
    if rootNodeKey == 0:
        rootNodeKey = nodeKey
        bst[nodeKey] = {"leftChild" : 0, "rightChild" : 0}
        continue

    nowNodeKey = rootNodeKey
    while nowNodeKey != 0:
        if nodeKey < nowNodeKey:
            if bst[nowNodeKey]["leftChild"] == 0:
                bst[nowNodeKey]["leftChild"] = nodeKey
                bst[nodeKey] = {"leftChild": 0,"rightChild" : 0}
            nowNodeKey = bst[nowNodeKey]["leftChild"]
        else: 
            if bst[nowNodeKey]["rightChild"] == 0:
                bst[nowNodeKey]["rightChild"] = nodeKey
                bst[nodeKey] = {"leftChild": 0,"rightChild" : 0}
            nowNodeKey = bst[nowNodeKey]["rightChild"]
travel(rootNodeKey)


    
