inputnums = input().split()
small = int(inputnums[0])
big = int(inputnums[1])
if  small > big:
    small,big = big,small
if small == big:
    print(0)
else:
    print(big-small-1)
for i in range(small+1,big):
    print(i,end=" ")