from sys import stdin
alphabetNums = [0]*26

for l in stdin.readline().strip():
    alphabetNums[ord(l)-ord("a")]+=1
for i in alphabetNums:
    print(i,end=" ") 
