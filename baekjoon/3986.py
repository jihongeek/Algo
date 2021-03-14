from sys import stdin

n = int(stdin.readline().strip())
goodWord = 0
for i in range(n):
    word = list(stdin.readline().strip())
    wordStack = []
    for i in word:
        if len(wordStack) > 0:
            if i == wordStack[-1]:
                wordStack.pop()
            else:
                wordStack.append(i)
        else:
            wordStack.append(i)
    if len(wordStack) == 0:
        goodWord+=1
print(goodWord)

            
        

        
