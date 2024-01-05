from sys import stdin,setrecursionlimit
setrecursionlimit(10**5)
"""
함수 호출 하고 반환될 때,
만약 두 노드 중 하나라면 반환하고
이미 한 노드를 찾았고 다른 노드를 찾았다면
그 단계에서의 노드가 NCA다!

예외 상황 : 만약에 부모노드가 두 노드 중 하나라면..?

케이스 생각:

현재 노드가 주어진 두 노드 중 하나일 경우 
-> 자식에서 반환 된 노드를 살펴보고, 주어진 노드가 없으면 자신 반환
-> 있으면 현재 노드가 NCA, 탐색 종료
반환된 노드 중에 주어진 두 노드 모두가 있을 경우 
-> 현재 노드가 NCA, 탐색 종료
반환된 노드 중에 주어진 두 노드 중 하나만 있을 경우 -> 해당 노드 반환
"""

def find_nca(now_node,first_child,second_child):
    children_found = []
    for child in tree[now_node]:
        returned_from_child = find_nca(child,first_child,second_child)
        returned_node,nca = returned_from_child
        if nca != None:
            return (now_node,nca)
        if returned_node in [first_child,second_child]:
            children_found.append(returned_node)
    # 주어진 두 노드중 한 노드가 자식에서 왔고 현재 노드가 두 노드 중 하나일 경우
    if (len(children_found) == 1 and 
        now_node in [first_child,second_child]):
        return (now_node,now_node)
    # 주어진 두 노드가 모두 자식에서 왔을 경우
    if len(children_found) == 2:
        return (now_node,now_node)
    # 주어진 두 노드 중 한 노드가 자식에서 왔고, 현재 노드가 두 노드중 한 노드가 아닐 경우  
    if len(children_found) == 1:
        return (children_found[0],None)
    return (now_node,None) 

t = int(stdin.readline().strip())
for test_case in range(t):
    n = int(stdin.readline().strip())
    tree = [[] for _ in range(n+1)]
    root = 0
    has_parent_list = [False]*(n+1)
    for edge in range(n-1):
        parent,child = map(int,stdin.readline().strip().split())
        has_parent_list[child] = True
        tree[parent].append(child)
    for node in range(1,n+1):
        if has_parent_list[node] is False:
            root = node
            break
    children_of_nca = map(int,stdin.readline().strip().split())
    first_child,second_child = children_of_nca
    print(find_nca(root,first_child,second_child)[1])
    

    

