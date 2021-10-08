from sys import stdin 
from math import sqrt
a,b = map(int,stdin.readline().strip().split())
palindromes = []
for i in range(a,b+1):
    isPalindrome = True
    numStr = str(i)
    for j in range(len(numStr)):
        if numStr[j] != numStr[len(numStr)-1-j]:
            isPalindrome = False
            break
    if isPalindrome:
        palindromes.append(i)


for palindrome in palindromes:
    isPrime = True
    for i in range(2,int(sqrt(palindrome))+1):
        if palindrome % i == 0:
            isPrime = False
            break
    if isPrime:
        print(palindrome) 
print(-1)