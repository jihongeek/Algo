from sys import stdin

"""
    전략 : 덧셈부터 계산하자
"""

expression_list = []
number_string = ""
for letter in stdin.readline().strip():
    if letter == "-" or letter == "+":
        expression_list.append(int(number_string))
        expression_list.append(letter)
        number_string = ""
    else:
        number_string += letter
expression_list.append(int(number_string))

result = expression_list[0]
temp = 0
is_minus_activated = False

for index in range(1,len(expression_list)):
    if expression_list[index] == "-":
        if is_minus_activated == False:
            result += temp
        else: 
            result -= temp
        temp = 0
        is_minus_activated = True
    elif expression_list[index] != "+":
        temp += expression_list[index]

if is_minus_activated == True:
    result -= temp
else:
    result += temp

print(result)
