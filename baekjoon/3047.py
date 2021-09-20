from sys import stdin 

numbers = list(map(int,stdin.readline().split()))
numbers.sort()

for char in stdin.readline().strip():
    print(numbers[ord(char) - ord('A')],end=" ")
