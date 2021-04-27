from sys import stdin
cases = 1
form = stdin.readline().strip()
isSame = False 

for i in range(0,len(form)):
    if form[i] == 'c':
        if isSame:
            cases *= 26 - 1 
        else:
            cases *= 26
        isSame = False
    else:
        if isSame:
            cases *= 10 - 1 
        else:
            cases *= 10
        isSame = False
    if i == len(form) - 1:
        break
    if form[i] == form[i+1]:
        isSame = True
print(cases)
    
