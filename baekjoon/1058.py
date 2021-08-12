from sys import stdin 

size = int(stdin.readline().strip())
friendNums = [0] * size
people = [stdin.readline().strip() for _ in range(size)] 
friendSetList = [None]*size
for i in range(size):
    friendSetList[i] = set()
    for j in range(size):
        if j != i and people[i][j] == "Y":
            friendSetList[i].add(j)
            for k in range(size):
                if k != i and k != j and people[j][k] == "Y":
                    friendSetList[i].add(k)
print(max([ len(friendSet) for friendSet in friendSetList]))

            
