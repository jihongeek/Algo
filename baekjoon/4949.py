from sys import stdin

"""
간단한 스택 문제?
-> 왼쪽 괄호이면 스택에 쌓고, 오른 쪽 괄호이면 제거
제거해야되는데 스택이 비었다?, 다 제거했는데 왼쪽 괄호가 남아있다? -> 불균형
"""

while True:
    isBalanced = True
    # 개행 컷
    given_string = stdin.readline().strip("\n")
    if given_string == ".":
        break
    bracket_stack = []
    for letter in given_string:
        if letter == "(" or letter == "[":
            bracket_stack.append(letter)
        elif letter == ")":
            if len(bracket_stack) == 0:
                isBalanced = False
                break
            if "(" != bracket_stack[-1]:
                isBalanced = False
                break
            bracket_stack.pop()
        elif letter == "]":
            if len(bracket_stack) == 0:
                isBalanced = False
                break
            if "[" != bracket_stack[-1]:
                isBalanced = False
                break
            bracket_stack.pop()
    if len(bracket_stack) > 0:
        isBalanced = False
    if isBalanced:
        print("yes")
    else:
        print("no")