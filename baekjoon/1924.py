import sys

inputstr = sys.stdin.readline().strip().split()
month = int(inputstr[0])
date = int(inputstr[1])

move_num = 0

month_monday = [1,2,3,4,5,6,0]
day = ['SUN','MON','TUE','WED','THU','FRI',"SAT"]
lastdate = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1,month):
    if i == 2:
        continue
    elif lastdate[i-1] == 30:
        move_num = move_num + 2
    else:
        move_num = move_num + 3

for i in range(move_num+1):
    new_month_monday = [int(month_monday[-1])]
    month_monday = month_monday[:-1]
    for i in month_monday:
        new_month_monday.append(i)
        month_monday = new_month_monday

print(day[month_monday.index(date % 7)])  
    