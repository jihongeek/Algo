from sys import stdin

n = int(stdin.readline().strip())
word = stdin.readline().strip()
sumOfhidden = 0
count = 0
for i in range(len(word)-1,-1,-1):
    if "0" <= word[i] <= "9":
        sumOfhidden += int(word[i])*(10**count)
        count += 1
    else:
        count = 0
print(sumOfhidden)

            
    


