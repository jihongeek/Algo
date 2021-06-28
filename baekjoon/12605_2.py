from sys import stdin
for i in range(int(stdin.readline().strip())):
    sentence = stdin.readline().strip().split()
    print(f"Case #{i+1}: ",end="")
    while len(sentence) > 0:
        print(sentence.pop(),end=" ")
    print()