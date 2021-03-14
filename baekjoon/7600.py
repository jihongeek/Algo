from string import ascii_lowercase

alphabets = list(ascii_lowercase)

while 1:
    count = 0
    inputstr = input()
    
    if inputstr == "#":
        break
    
    inputstr = inputstr.lower()

    for i in alphabets:
        if i in inputstr:
            count = count + 1
    print(count)
            

    