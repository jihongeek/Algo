from sys import stdin

def sumDigit(serial):
    sumOfDigit = 0
    for letter in serial:
        if '0' <= letter <= '9':
            sumOfDigit += int(letter)
    return sumOfDigit

n = int(stdin.readline().strip())
serials = [ stdin.readline().strip() for _ in range(n) ] 

for i in range(n-1):
    for j in range(n-1):
        if len(serials[j]) > len(serials[j+1]):
            serials[j],serials[j+1] = serials[j+1],serials[j]
        elif len(serials[j]) == len(serials[j+1]):
            if sumDigit(serials[j]) > sumDigit(serials[j+1]):
                serials[j],serials[j+1] = serials[j+1],serials[j]
            elif sumDigit(serials[j]) == sumDigit(serials[j+1]):
                if serials[j] > serials[j+1]: 
                    serials[j],serials[j+1] = serials[j+1],serials[j]

for i in serials:
    print(i)
                
