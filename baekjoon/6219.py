import math
inputnums = input().split()
a = int(inputnums[0])
b = int(inputnums[1])
d = inputnums[2]
numbers = []
count = 0
for i in range(2,b+1):
    numbers.append(i)
for i in range(0,round(math.sqrt(b))):
    print(i+(j)*numbers[i])
    if numbers[i] == 0:
        continue
    for j in range(1,int(b/numbers[i])+1):
        if numbers[i+(j)*numbers[i]] == 0:
            continue
        else:
            numbers[i+(j)*numbers[i]] =0
for i in range(0,b):
    if numbers[i]!=0 and numbers[i]>=a:
        if d in str(numbers[i]):
            count = count + 1
print(str(count)+"\n")