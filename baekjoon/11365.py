from sys import stdin

while True:
    code = stdin.readline().strip()
    if code == 'END':
        break
    else:
        print("".join(reversed(code)))