inputstr = input().split()

decnum = int(inputstr[0])
to = int(inputstr[1])
digits = []
modednums = []

for i in range(0,10):
    digits.append(f"{i}")

for i in range(65,91):
    digits.append("%c"%i)

while decnum:
    modednums.append(digits[(decnum % to)])    
    decnum = int(decnum/to)
print("".join(reversed(modednums)))
