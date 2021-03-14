import sys

inputnum = int(input())
peoples = set()

for i in range(inputnum):
    command = sys.stdin.readline().strip().split()
    name = command[0]
    behavior = command[1]
    if behavior == "enter":
        peoples.add(name)
    else:
        peoples.remove(name)
peoples = sorted(list(peoples),reverse=True)
for i in peoples:
    print(i)