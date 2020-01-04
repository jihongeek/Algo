allnums = list(range(1,10001))
def d(n):
    return n + sum(list(map(int,str(n))))
for i in range(1,10001):
    if d(i) in allnums:
        allnums.remove(d(i))
for i in allnums:
    print(i)