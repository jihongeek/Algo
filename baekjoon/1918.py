from sys import stdin

infix_expression = stdin.readline().strip()
postfix_expression = ""
operator_stack = []

# 연산자를 Key로 갖고 우선 순위를 Value로 같는 딕서너리 
operator_dict = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "(" : 0,
    ")" : 0
}
for character in infix_expression:
    if character not in operator_dict:
        postfix_expression += character
    else:
        if len(operator_stack) == 0:
            operator_stack.append(character)
            continue
        elif character == "(":
            operator_stack.append(character)
            continue
        elif character == ")":
            while operator_stack[-1] != "(":
                postfix_expression += operator_stack.pop()
            operator_stack.pop()
            continue
        elif operator_dict[operator_stack[-1]] >= operator_dict[character]:
            while len(operator_stack) > 0 and operator_dict[operator_stack[-1]] >= operator_dict[character]:
                postfix_expression += operator_stack.pop()
            operator_stack.append(character)
        else:
            operator_stack.append(character)

while len(operator_stack) > 0:
    postfix_expression += operator_stack.pop()
print(postfix_expression)