from sys import stdin
problem = 0
start = stdin.readline().strip()
while True:
    sentence = stdin.readline().strip()
    if sentence == "문제":
        problem += 1
    elif sentence == "고무오리":
        if problem == 0:
            problem += 2
            continue
        problem = problem - 1
    else:
        break
if problem == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")