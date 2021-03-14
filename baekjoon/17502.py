num = int(input())
strlist = list(input())
for i in range(num):
    if strlist[i] == '?' and strlist[-i-1] == '?':
        strlist[i] = 'k'
        strlist[-i-1] = 'k'
    elif strlist[i] != '?' and strlist[-i-1] == '?':
        strlist[-i-1] = strlist[i] 
    elif strlist[i] == '?' and strlist[-i-1] != '?': 
        strlist[i] = strlist[-i-1]
print("".join(strlist))
    