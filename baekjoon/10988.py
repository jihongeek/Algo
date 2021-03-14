inputstr = input()
isPalindrome = 1
for i in range(int(len(inputstr)/2)):
    if inputstr[i] != inputstr[-i-1]:
        isPalindrome = 0
        break
print(isPalindrome)

        