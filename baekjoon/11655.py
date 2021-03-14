from string import ascii_lowercase,ascii_uppercase

inputstr = input()

alphabet_u = ascii_uppercase
alphabet_l = ascii_lowercase

for i in range(len(inputstr)):
    if inputstr[i] in alphabet_u:
        now_i = alphabet_u.index(inputstr[i])
        if now_i + 13 > 25:
            now_i = now_i + 13 - 26
        else:
            now_i = now_i + 13
        inputstr = inputstr[:i] + alphabet_u[now_i] + inputstr[i+1:]
    elif inputstr[i] in alphabet_l:
        now_i = alphabet_l.index(inputstr[i])
        if now_i + 13 > 25:
            now_i = now_i + 13 - 26
        else:
            now_i = now_i + 13
        inputstr = inputstr[:i] + alphabet_l[now_i] + inputstr[i+1:]
print(inputstr)