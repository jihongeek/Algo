import string
alphabet  = string.ascii_lowercase
inputstr = input().lower()
countlist = []
for i in range(0,26):
    countlist.append(0)
for i,k in enumerate(alphabet):
    for j in inputstr:
        if j == k:
            countlist[i] = countlist[i]+1
sortedcountlist = sorted(countlist)
if sortedcountlist[-1] == sortedcountlist[-2]:
    print("?")
else:
    print(alphabet[countlist.index(sortedcountlist[-1])].upper())
