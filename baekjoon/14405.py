inputstr = input()
pikachu = ["pi","ka","chu"]

isPossible = True

for i in pikachu:
    if i in inputstr:
        inputstr = inputstr.replace(i,"X"*len(i))

for i in inputstr:
    if i != "X":
        isPossible = False
        break
    
if isPossible:
    print("YES")
else:
    print("NO")