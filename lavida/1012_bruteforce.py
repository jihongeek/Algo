from sys import stdin
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def changeVolume(nowV,vIndex):
    global n , volumes,m,maxOfVolume
    if vIndex == n - 1:
        maxOfVolume = max(maxOfVolume,nowV)
        return 
    if nowV + volumes[vIndex+1] <= m:
        changeVolume(nowV + volumes[vIndex+1],vIndex+1) 
    if 0 <= nowV - volumes[vIndex+1]:
        changeVolume(nowV - volumes[vIndex+1],vIndex+1) 

for testcase in range(int(stdin.readline().strip())):
    maxOfVolume = -1
    n,s,m = map(int,stdin.readline().strip().split())
    volumes = list(map(int,stdin.readline().strip().split()))
    changeVolume(s,-1)
    print(maxOfVolume)