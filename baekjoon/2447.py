# 이전 패턴을 받아서 재귀적으로 새로운 별찍기 패턴을 생성하는 함수  
def make_pattern(last_pattern,last_n,n):
    if last_n == n:
        return last_pattern
    new_pattern = ""
    pattern_lines = last_pattern.split("\n")
    # 상단 라인 
    for index,character in enumerate(pattern_lines):
        new_pattern += (character * 3 + "\n")  
    # 중간 라인
    for character in last_pattern.split("\n"):
        new_pattern += (character + " "*last_n + character + "\n")
    # 하단 라인
    for index,character in enumerate(pattern_lines):
        new_pattern += (character * 3)
        if index < len(pattern_lines) - 1:
            new_pattern += "\n"

    return make_pattern(new_pattern,last_n*3,n)

print(make_pattern("*",1,int(input())))
    
    
     