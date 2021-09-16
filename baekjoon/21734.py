from sys import stdin

for char in stdin.readline().strip():
    charNum = ord(char)
    asciiDigitSum = 0
    while charNum > 0:
        asciiDigitSum += (charNum % 10)
        charNum //= 10  
    print(f"{char}"* asciiDigitSum)