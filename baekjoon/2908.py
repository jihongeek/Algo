q = input().split()
a = int("".join(reversed(list(q[0]))))
b = int("".join(reversed(list(q[1]))))
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(a)

