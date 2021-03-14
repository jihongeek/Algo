import re

varName = input()
varname = varName
isJava = False
isCplus = False
isError = False

if re.match("[A-Z]|_",varName[0]) or re.match("_",varName[-1]) or re.search("__",varName) or re.search("_[A-Z]",varName):
    isError = True
else:
    if re.search("_[a-z]",varName):
        isCplus = True
    if re.search("[A-Z]",varName):
        isJava = True
    if isCplus and isJava:
        isError = True

if isError:
    print('Error!')
elif isJava:
    for i in re.finditer("[A-Z]",varName):
        start,end = i.span()
        matched = varName[start:end]
        varname = re.sub(f"{matched}",'_'+matched.lower(),varname)
    print(varname)
elif isCplus:
    for i in re.finditer("_[a-z]",varName):
        start,end = i.span()
        matched = varName[start:end]
        varname = re.sub(f"{matched}",matched[-1].upper(),varname)
    print(varname)
else:
    print(varname)
