while 1:
    inputnum = input()
    if inputnum == "0":
        break
    first = ""
    second = ""
    inputnums = list(map(int,inputnum[1:].split()))
    inputnums.sort()
    for i in inputnums:
        if first == "" and i == 0:
            continue
        first = first + str(i)
    print(first)


        