from sys import stdin

case = 1
while True:
    l,p,v = map(int,stdin.readline().strip().split())
    if l+p+v == 0:
        break
    if v%p > l:
        print(f"Case {case}: {v//p*l + l}")
    else:    
        print(f"Case {case}: {v//p*l + v%p}")
    case+=1