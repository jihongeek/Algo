from sys import stdin

"""
    전공평점 = 전공과목별 (학점 * 과목평점) 합을 / 학점의 총합
    but P 과목 제외
"""

sum_of_grade = 0
sum_of_credit = 0

for _ in range(20):
    subject_name, subject_credit, subject_grade = stdin.readline().strip().split()
    subject_credit = float(subject_credit)
    if subject_grade[0] == "P":
        continue
    elif subject_grade[0] == "F":
        sum_of_grade += 0.0
        sum_of_credit += subject_credit
        continue
    else:
        subject_grade_score = 4 - (ord(subject_grade[0]) - ord("A"))
    if subject_grade[1] == "+":
        subject_grade_score += 0.5
    sum_of_grade += subject_grade_score * subject_credit
    sum_of_credit += subject_credit    
print(sum_of_grade / sum_of_credit)