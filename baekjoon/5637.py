from sys import stdin 

longest = ""
inputText = stdin.read().strip()
newText = ""
for char in inputText:
    if not ("A" <= char <= "Z" or char == "-" or "a" <= char <= "z"):
        newText += " "
    else:
        newText += char  
for word in newText.split():
    isWord = True
    if word == "E-N-D":
        break
    if len(longest) < len(word):
        longest = word
print(longest.lower())