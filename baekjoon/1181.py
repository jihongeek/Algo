import sys 

inputnum = int(sys.stdin.readline().strip())
words = {}
max = 0
for i in range(inputnum):
    word = sys.stdin.readline().strip()
    length = len(word)
    if length in words:
        words[length].append(word)
    else:
        words[length] = [word]
lenlist = sorted(list(words.keys()))
for i in lenlist:
    words[i] = sorted(list(set(words[i])))

for i in lenlist:
    for j in words[i]:
        print(j)

