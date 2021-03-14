inputstr = input()

decnum = int(inputstr)
digits = ["0","1"]
modednums = []
while decnum:
    modednums.append(digits[(decnum % 2)])    
    decnum = int(decnum/2)
print("".join(reversed(modednums)))