while True:
    inputstr = input()
    if inputstr == "0":
        break
    isPalindrome = "yes"
    for i in range(int(len(inputstr)/2)):
        if inputstr[i] != inputstr[-i-1]:
            isPalindrome = "no"
            break
    print(isPalindrome)