cr_alphabets = ['c=','c-','dz=','d-','lj','nj','s=','z=']
inputstr = "ddz=z="
for i in cr_alphabets:
    if i in inputstr:
        inputstr = inputstr.replace(i," ")
        print(inputstr)
print(len(inputstr))
