from sys import stdin 
charDict = {}
charFrequencyDict = {}
for asciiNum in range(ord('A'),ord('Z')+1):
    charFrequencyDict[chr(asciiNum)] = 0

nowNum = 9
sumOfWords = 0
n = int(stdin.readline().strip())
words = [stdin.readline().strip() for _ in range(n)]

for word in words:
    wordLength = len(word)
    for index,char in enumerate(word):
        charFrequencyDict[char] += 10**(wordLength-1-index)
charFrequencyList = sorted(charFrequencyDict.items(), key = lambda item : item[1], reverse= True)

for char,_ in charFrequencyList:
    if charFrequencyDict[char] > 0:
        charDict[char] = nowNum
        nowNum -= 1
    else:
        charDict[char] = 0

for word in words:
    wordLength = len(word)
    for index,char in enumerate(word):
        if char in charDict:
            sumOfWords += charDict[char]*10**(wordLength-1-index)
print(sumOfWords)
