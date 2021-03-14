from sys import stdin
# 피연산자의 대응하는 숫자의 갯수 입력받아 저장 
n = int(stdin.readline().strip())

# 후위표기식을 입력 받아서 저장  
postfix = list(stdin.readline().strip())
# 스택으로 사용할 리스트 하나 만들기 
stack = [] 
# 피연산자에 대응하는 숫자들을 n 만큼 입력 받아 저장 
numbers = [int(stdin.readline().strip()) for _ in range(n)]

for i in range(len(postfix)):
    # 후위 표기식의 피연산자를 해당하는 숫자로 바꾸기   
    if "A" <= postfix[i] <= "Z":
        postfix[i] = numbers[ord(postfix[i]) - ord('A')]
# 후위 표기식의 문자를 하나씩 가져와서 연산 진행 
for i in postfix:
    # 숫자면 스택에 넣고(push) 연산자면 2개의 숫자를 꺼내서(pop) 연산하고 넣기(push) 
    if i == '+':
        stack.append(stack.pop() + stack.pop())
    # 뺄셈과 나눗셈은 교환법칙이 성립하지 않으므로 원래 계산 순서! 
    elif i == '-':
        second = stack.pop()
        first = stack.pop()
        stack.append(first - second)
    elif i == '*':
        stack.append(stack.pop() * stack.pop())
    elif i == '/':
        second = stack.pop()
        first = stack.pop()
        stack.append(first / second)
    else:
        stack.append(i)
# 스택에 남아있는 숫자 소수 둘째 자리까지 출력    
print("%.2f"%stack[0])