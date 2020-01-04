import string 
alphabet = string.ascii_lowercase
inputstr = input()
outputlist =[]
for i in alphabet:
    if i in inputstr:
        outputlist.append(str(inputstr.index(i)))
    else:
        outputlist.append("-1")
print(" ".join(outputlist))

