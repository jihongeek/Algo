words = []
inputnum = int(input())
for i in range(inputnum):
    words.append(input())
for i in words:
    if "".join(reversed(i)) in words:
        print(len(i),i[int(len(i)/2)])
        break
    