from string import ascii_lowercase
from sys import stdin
l,c = map(int, stdin.readline().strip().split())
characters = sorted(stdin.readline().strip().split())

def findPassword(chosen):
    if len(chosen) == l:
        vowel = 0
        consonant = 0
        for i in chosen:
            if i in ['a','e','i','o','u']:
                vowel += 1
            else:
                consonant += 1
            if vowel >= 1 and consonant >= 2:
                print(chosen)
                return
        return
    else:
        for i in range(c): 
            if len(chosen) == 0:
                findPassword(chosen + characters[i])
            elif characters[i] not in chosen:
                findPassword(chosen + characters[i])

findPassword("")